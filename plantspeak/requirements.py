from __future__ import annotations

import json
from importlib.resources import files
from typing import Any


def load_requirements() -> list[dict[str, Any]]:
    data = files("plantspeak.data").joinpath("requirements.json").read_text(encoding="utf-8")
    return json.loads(data)


def load_issue_links() -> list[dict[str, Any]]:
    data = files("plantspeak.data").joinpath("issue_links.json").read_text(encoding="utf-8")
    return json.loads(data)


def requirement_ids() -> set[str]:
    return {str(requirement["id"]) for requirement in load_requirements()}


def ordered_requirement_ids() -> list[str]:
    return [str(requirement["id"]) for requirement in load_requirements()]


def requirement_by_id(requirement_id: str) -> dict[str, Any]:
    for requirement in load_requirements():
        if requirement["id"] == requirement_id:
            return requirement
    raise KeyError(requirement_id)
