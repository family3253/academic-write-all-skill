from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path
from typing import Any, Callable, Final, cast

import requests

common_module = importlib.import_module(
    ".awas_runtime_common" if __package__ else "awas_runtime_common",
    package=__package__,
)
env_or_value: Final[Callable[[str | None, str, str], str]] = cast(
    Callable[[str | None, str, str], str], common_module.env_or_value
)
expand_path: Final[Callable[[str], Path]] = cast(
    Callable[[str], Path], common_module.expand_path
)
load_json: Final[Callable[[Path], Any]] = cast(
    Callable[[Path], Any], common_module.load_json
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
        description="Create Zotero items from a JSON payload through the Web API."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to a JSON file containing a list of Zotero item payloads.",
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
    input_path = expand_path(args.input)
    payload = load_json(input_path)
    if not isinstance(payload, list):
        raise SystemExit("Input JSON must be a list of Zotero item payload objects.")

    response = requests.post(
        f"{zotero_base_url(user_id, library_type)}/items",
        headers=zotero_headers(api_key),
        data=json.dumps(payload, ensure_ascii=False),
        timeout=30,
    )
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    main()
