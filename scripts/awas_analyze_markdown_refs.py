from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze in-text citation coverage against a numbered markdown reference list."
    )
    parser.add_argument("markdown_path", help="Markdown file to inspect.")
    parser.add_argument(
        "--section-marker",
        default="参考文献（前言部分）",
        help="Marker text that splits the main body from the numbered references section.",
    )
    parser.add_argument(
        "--preview-count",
        type=int,
        default=8,
        help="Number of reference entries to include in entries_preview.",
    )
    args = parser.parse_args()

    path = Path(args.markdown_path).expanduser().resolve()
    text = path.read_text(encoding="utf-8")
    if args.section_marker not in text:
        raise SystemExit(f"Section marker not found: {args.section_marker}")
    body, refs = text.split(args.section_marker, 1)

    citation_tokens = re.findall(r"\\\[([^\]]+)\\\]", body)
    body_ids: set[int] = set()
    for token in citation_tokens:
        token = token.replace("，", ",").replace(" ", "")
        for part in token.split(","):
            if not part:
                continue
            if "-" in part:
                start, end = part.split("-", 1)
                if start.isdigit() and end.isdigit():
                    body_ids.update(range(int(start), int(end) + 1))
            elif part.isdigit():
                body_ids.add(int(part))

    entry_matches = list(re.finditer(r"(?m)^\\\[(\d+)\\\]\s*", refs))
    entry_ids = [int(match.group(1)) for match in entry_matches]
    entries: list[dict[str, object]] = []
    for index, match in enumerate(entry_matches):
        start = match.end()
        end = (
            entry_matches[index + 1].start()
            if index + 1 < len(entry_matches)
            else len(refs)
        )
        content = " ".join(refs[start:end].split())
        entries.append({"id": int(match.group(1)), "text": content})

    report = {
        "markdown_path": str(path),
        "section_marker": args.section_marker,
        "body_citation_count": len(body_ids),
        "body_citation_ids": sorted(body_ids),
        "reference_entry_count": len(entry_ids),
        "reference_entry_ids": entry_ids,
        "missing_in_reference": sorted(body_ids - set(entry_ids)),
        "unused_reference_entries": sorted(set(entry_ids) - body_ids),
        "entries_preview": entries[: args.preview_count],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
