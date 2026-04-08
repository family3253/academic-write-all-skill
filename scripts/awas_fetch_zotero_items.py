from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path
from typing import Callable, Final, cast

import requests

common_module = importlib.import_module(
    ".awas_runtime_common" if __package__ else "awas_runtime_common",
    package=__package__,
)
env_or_value: Final[Callable[[str | None, str, str], str]] = cast(
    Callable[[str | None, str, str], str], common_module.env_or_value
)
ensure_parent: Final[Callable[[Path], Path]] = cast(
    Callable[[Path], Path], common_module.ensure_parent
)
expand_path: Final[Callable[[str], Path]] = cast(
    Callable[[str], Path], common_module.expand_path
)
require_env_or_value: Final[Callable[[str | None, str], str]] = cast(
    Callable[[str | None, str], str], common_module.require_env_or_value
)
zotero_base_url: Final[Callable[[str, str], str]] = cast(
    Callable[[str, str], str], common_module.zotero_base_url
)
zotero_headers: Final[Callable[[str], dict[str, str]]] = cast(
    Callable[[str], dict[str, str]], common_module.zotero_headers
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch Zotero items by key through the Web API and save them as JSON."
    )
    parser.add_argument(
        "--item",
        action="append",
        required=True,
        help="Zotero item key. Repeat for multiple items.",
    )
    parser.add_argument(
        "--output", required=True, help="Path to the JSON file to write."
    )
    parser.add_argument(
        "--api-key", default="", help="Zotero API key. Falls back to ZOTERO_API_KEY."
    )
    parser.add_argument(
        "--user-id", default="", help="Zotero user ID. Falls back to ZOTERO_USER_ID."
    )
    parser.add_argument(
        "--library-type",
        default="",
        help="Zotero library type (user or group). Falls back to ZOTERO_LIBRARY_TYPE or 'user'.",
    )
    args = parser.parse_args()

    api_key = require_env_or_value(args.api_key, "ZOTERO_API_KEY")
    user_id = require_env_or_value(args.user_id, "ZOTERO_USER_ID")
    library_type = env_or_value(args.library_type, "ZOTERO_LIBRARY_TYPE", "user")
    base_url = zotero_base_url(user_id, library_type)
    headers = zotero_headers(api_key)

    items: list[dict[str, object]] = []
    for item_key in args.item:
        response = requests.get(
            f"{base_url}/items/{item_key}", headers=headers, timeout=30
        )
        response.raise_for_status()
        items.append(response.json()["data"])

    output_path = ensure_parent(expand_path(args.output))
    output_path.write_text(
        json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[ok] wrote {len(items)} item(s) to {output_path}")


if __name__ == "__main__":
    main()
