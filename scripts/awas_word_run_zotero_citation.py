from __future__ import annotations

import argparse
import json


def require_word():
    try:
        import win32com.client as win32  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "pywin32 is required for Word automation. Install the runtime on Windows and retry."
        ) from exc
    return win32


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Insert an optional anchor and invoke ZoteroAddEditCitation in the active Word document."
    )
    parser.add_argument(
        "--anchor-text",
        default="[AWAS-Zotero-citation-test-anchor]",
        help="Anchor text inserted before invoking ZoteroAddEditCitation. Pass an empty string to skip insertion.",
    )
    args = parser.parse_args()

    win32 = require_word()
    app = win32.Dispatch("Word.Application")
    doc = app.ActiveDocument
    selection = app.Selection

    if args.anchor_text:
        selection.EndKey(Unit=6)
        selection.TypeParagraph()
        selection.TypeText(args.anchor_text)
        selection.TypeParagraph()

    payload = {
        "macro": "ZoteroAddEditCitation",
        "result": "RUN_OK",
        "error": "",
        "fields": doc.Fields.Count,
        "bookmarks": doc.Bookmarks.Count,
        "variables": doc.Variables.Count,
    }
    try:
        app.Run("ZoteroAddEditCitation")
    except (
        Exception
    ) as exc:  # pragma: no cover - COM error surface is runtime-dependent
        payload["result"] = "RUN_ERR"
        payload["error"] = str(exc)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
