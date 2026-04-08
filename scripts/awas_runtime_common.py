from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_ROOT / "assets" / "templates"


def expand_path(raw: str) -> Path:
    return Path(raw).expanduser().resolve()


def ensure_parent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def env_or_value(value: str | None, env_name: str, default: str = "") -> str:
    if value:
        return value
    env_value = os.environ.get(env_name, "").strip()
    if env_value:
        return env_value
    return default


def require_env_or_value(value: str | None, env_name: str) -> str:
    resolved = env_or_value(value, env_name)
    if resolved:
        return resolved
    raise SystemExit(
        f"Missing required value. Pass the CLI argument explicitly or set environment variable {env_name}."
    )


def zotero_headers(api_key: str) -> dict[str, str]:
    return {
        "Zotero-API-Key": api_key,
        "Zotero-API-Version": "3",
        "Content-Type": "application/json",
    }


def zotero_base_url(user_id: str, library_type: str = "user") -> str:
    return f"https://api.zotero.org/{library_type}s/{user_id}"


def sample_template_path(name: str) -> Path:
    return TEMPLATES_DIR / name
