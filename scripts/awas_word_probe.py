from __future__ import annotations

import argparse
import json
from typing import Any


def require_word() -> Any:
    try:
        import win32com.client as win32  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "pywin32 is required for Word automation. Install the runtime on Windows and retry."
        ) from exc
    return win32


def word_app() -> Any:
    win32 = require_word()
    return win32.Dispatch("Word.Application")


def active_document() -> Any:
    app = word_app()
    try:
        return app, app.ActiveDocument
    except (
        Exception
    ) as exc:  # pragma: no cover - COM error surface is runtime-dependent
        raise SystemExit(f"Could not access the active Word document: {exc}") from exc


def cmd_docmeta(_args: argparse.Namespace) -> int:
    app, doc = active_document()
    payload = {
        "document": doc.Name,
        "fields": doc.Fields.Count,
        "bookmarks": doc.Bookmarks.Count,
        "variables": doc.Variables.Count,
        "visible": bool(app.Visible),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def cmd_addins(_args: argparse.Namespace) -> int:
    app = word_app()
    items = []
    for index in range(1, app.AddIns.Count + 1):
        addin = app.AddIns.Item(index)
        items.append(
            {
                "name": addin.Name,
                "path": getattr(addin, "Path", ""),
                "installed": bool(getattr(addin, "Installed", False)),
            }
        )
    print(json.dumps(items, ensure_ascii=False, indent=2))
    return 0


def cmd_commandbars(args: argparse.Namespace) -> int:
    app = word_app()
    items = []
    limit = args.limit
    for index in range(1, min(app.CommandBars.Count, limit) + 1):
        bar = app.CommandBars.Item(index)
        items.append({"name": bar.Name, "visible": bool(bar.Visible)})
    print(json.dumps(items, ensure_ascii=False, indent=2))
    return 0


def cmd_macros(_args: argparse.Namespace) -> int:
    app = word_app()
    payload = {
        "automation_security": getattr(app, "AutomationSecurity", None),
        "macro_container": getattr(app, "MacroContainer", ""),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def cmd_zotero_state(args: argparse.Namespace) -> int:
    _app, doc = active_document()
    variables = []
    for index in range(1, min(doc.Variables.Count, args.limit) + 1):
        variable = doc.Variables.Item(index)
        value = variable.Value
        preview = value[: args.preview_chars] if isinstance(value, str) else value
        variables.append({"name": variable.Name, "value_preview": preview})
    payload = {
        "document": doc.Name,
        "fields": doc.Fields.Count,
        "bookmarks": doc.Bookmarks.Count,
        "variables": doc.Variables.Count,
        "variables_preview": variables,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def cmd_dump_fields(args: argparse.Namespace) -> int:
    _app, doc = active_document()
    fields = []
    for index in range(1, min(doc.Fields.Count, args.limit) + 1):
        field = doc.Fields.Item(index)
        fields.append(
            {
                "index": index,
                "code": getattr(field.Code, "Text", "").strip(),
                "result": getattr(field.Result, "Text", "").strip()[
                    : args.preview_chars
                ],
            }
        )
    print(json.dumps(fields, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Probe the current Microsoft Word automation state for AWAS workflows."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    docmeta = subparsers.add_parser(
        "docmeta", help="Show top-level metadata for the active Word document."
    )
    docmeta.set_defaults(func=cmd_docmeta)

    addins = subparsers.add_parser("addins", help="List installed Word add-ins.")
    addins.set_defaults(func=cmd_addins)

    commandbars = subparsers.add_parser(
        "commandbars", help="List the first N Word command bars."
    )
    commandbars.add_argument("--limit", type=int, default=20)
    commandbars.set_defaults(func=cmd_commandbars)

    macros = subparsers.add_parser(
        "macros", help="Inspect Word macro-related automation state."
    )
    macros.set_defaults(func=cmd_macros)

    zotero_state = subparsers.add_parser(
        "zotero-state",
        help="Inspect fields, bookmarks, and the first N document variables for Zotero automation debugging.",
    )
    zotero_state.add_argument("--limit", type=int, default=20)
    zotero_state.add_argument("--preview-chars", type=int, default=200)
    zotero_state.set_defaults(func=cmd_zotero_state)

    dump_fields = subparsers.add_parser(
        "dump-fields", help="Dump the first N Word field codes and results."
    )
    dump_fields.add_argument("--limit", type=int, default=50)
    dump_fields.add_argument("--preview-chars", type=int, default=200)
    dump_fields.set_defaults(func=cmd_dump_fields)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
