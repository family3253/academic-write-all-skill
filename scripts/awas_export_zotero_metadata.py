from __future__ import annotations

import argparse
import importlib
import json
import subprocess
from pathlib import Path
from typing import Any, Callable, Final, cast

common_module = importlib.import_module(
    ".awas_runtime_common" if __package__ else "awas_runtime_common",
    package=__package__,
)
ensure_parent: Final[Callable[[Path], Path]] = cast(
    Callable[[Path], Path], common_module.ensure_parent
)
expand_path: Final[Callable[[str], Path]] = cast(
    Callable[[str], Path], common_module.expand_path
)


FORMAT_EXTENSIONS = {
    "markdown": "md",
    "bibtex": "bib",
}


def parse_item(raw: str) -> tuple[str, str]:
    if "=" not in raw:
        raise SystemExit(
            "--item must use label=item_key format, for example journal=7DIDVIGX"
        )
    label, item_key = raw.split("=", 1)
    label = label.strip()
    item_key = item_key.strip()
    if not label or not item_key:
        raise SystemExit("--item requires both a non-empty label and item key")
    return label, item_key


def run_fastmcp(config_path: Path, item_key: str, output_format: str) -> str:
    cmd = [
        "uvx",
        "fastmcp",
        "call",
        str(config_path),
        "--target",
        "zotero_get_item_metadata",
        "--input-json",
        json.dumps(
            {
                "item_key": item_key,
                "include_abstract": True,
                "format": output_format,
            },
            ensure_ascii=False,
        ),
        "--json",
    ]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    if proc.returncode != 0:
        raise SystemExit(
            f"fastmcp failed for {item_key}/{output_format}: {stderr or stdout}"
        )
    start = stdout.find("{")
    end = stdout.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise SystemExit(
            f"Could not locate JSON payload in stdout for {item_key}/{output_format}:\n{stdout}"
        )
    payload = json.loads(stdout[start : end + 1])
    return payload["structured_content"]["result"]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export Zotero item metadata through fastmcp into Markdown/BibTeX artifacts."
    )
    parser.add_argument(
        "--config", required=True, help="Path to a fastmcp Zotero config JSON file"
    )
    parser.add_argument(
        "--item",
        action="append",
        required=True,
        help="Item mapping in label=item_key format. Repeat for multiple items.",
    )
    parser.add_argument(
        "--format",
        action="append",
        choices=sorted(FORMAT_EXTENSIONS),
        help="Output format(s). Defaults to markdown and bibtex.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs/awas-mcp-exports",
        help="Directory where exported artifacts and summary.json will be written.",
    )
    args = parser.parse_args()

    config_path = expand_path(args.config)
    output_dir = expand_path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    formats = args.format or ["markdown", "bibtex"]
    items = [parse_item(raw) for raw in args.item]

    summary: dict[str, dict[str, Any]] = {}
    for label, item_key in items:
        summary_entry: dict[str, Any] = {"item_key": item_key, "outputs": {}}
        summary[label] = summary_entry
        for output_format in formats:
            rendered = run_fastmcp(config_path, item_key, output_format)
            extension = FORMAT_EXTENSIONS[output_format]
            output_path = ensure_parent(output_dir / f"{label}_{item_key}.{extension}")
            output_path.write_text(rendered, encoding="utf-8")
            outputs = cast(dict[str, str], summary_entry["outputs"])
            outputs[output_format] = str(output_path)
            if output_format == "markdown":
                summary_entry["markdown_has_title"] = rendered.lstrip().startswith("# ")
                summary_entry["markdown_has_identifier"] = "**Item Key:**" in rendered
            if output_format == "bibtex":
                summary_entry["bibtex_starts_with_entry"] = (
                    rendered.lstrip().startswith("@")
                )
                summary_entry["bibtex_has_title_field"] = "title = {" in rendered

    summary_path = output_dir / "summary.json"
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
