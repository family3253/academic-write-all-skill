from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def parse_ids(raw_ids: list[str]) -> list[int]:
    parsed: list[int] = []
    for raw in raw_ids:
        for part in raw.split(","):
            token = part.strip()
            if not token:
                continue
            if not token.isdigit():
                raise SystemExit(f"Reference id must be numeric, got: {token}")
            parsed.append(int(token))
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract selected numbered reference entries from a markdown references section."
    )
    parser.add_argument("markdown_path", help="Markdown file to inspect.")
    parser.add_argument(
        "--section-marker",
        default="参考文献（前言部分）",
        help="Marker text that precedes the numbered references section.",
    )
    parser.add_argument(
        "--ref-id",
        action="append",
        required=True,
        help="Reference id(s) to extract. Repeat or pass comma-separated ids.",
    )
    args = parser.parse_args()

    wanted_ids = set(parse_ids(args.ref_id))
    path = Path(args.markdown_path).expanduser().resolve()
    text = path.read_text(encoding="utf-8")
    if args.section_marker not in text:
        raise SystemExit(f"Section marker not found: {args.section_marker}")
    refs = text.split(args.section_marker, 1)[1]
    entry_matches = list(re.finditer(r"(?m)^\\\[(\d+)\\\]\s*", refs))

    entries: dict[int, str] = {}
    for index, match in enumerate(entry_matches):
        ref_id = int(match.group(1))
        start = match.end()
        end = (
            entry_matches[index + 1].start()
            if index + 1 < len(entry_matches)
            else len(refs)
        )
        content = " ".join(refs[start:end].split())
        if ref_id in wanted_ids:
            entries[ref_id] = content

    payload = {
        "markdown_path": str(path),
        "section_marker": args.section_marker,
        "requested_ids": sorted(wanted_ids),
        "resolved_entries": [
            {"reference_id": ref_id, "raw_reference": entries.get(ref_id, "")}
            for ref_id in sorted(wanted_ids)
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
