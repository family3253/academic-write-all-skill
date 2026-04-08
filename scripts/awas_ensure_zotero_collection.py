from __future__ import annotations

import argparse
import importlib
import json
from typing import Callable, Final, cast

import requests


common_module = importlib.import_module(
    ".awas_runtime_common" if __package__ else "awas_runtime_common",
    package=__package__,
)
env_or_value: Final[Callable[[str | None, str, str], str]] = cast(
    Callable[[str | None, str, str], str], common_module.env_or_value
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
        description="Ensure a top-level Zotero collection exists and return its key."
    )
    parser.add_argument(
        "--name", required=True, help="Top-level collection name to ensure."
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

    existing = requests.get(f"{base_url}/collections/top", headers=headers, timeout=30)
    existing.raise_for_status()
    for collection in existing.json():
        data = collection["data"]
        if data["name"] == args.name:
            print(
                json.dumps(
                    {
                        "status": "exists",
                        "key": collection["key"],
                        "name": data["name"],
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return

    payload = [{"name": args.name, "parentCollection": False}]
    response = requests.post(
        f"{base_url}/collections",
        headers=headers,
        data=json.dumps(payload, ensure_ascii=False),
        timeout=30,
    )
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    main()
