from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal


RequirementStatus = Literal["modeled", "canned-data", "dev-board-led-substitute", "dev-board-unavailable", "hardware"]
EvidenceStage = Literal["S1", "S2", "S3", "S4", "S5", "S6", "S7"]


@dataclass(frozen=True)
class RequirementContract:
    requirement_id: str
    issue_number: int | None
    command: str
    status: RequirementStatus
    code_modules: tuple[str, ...]
    unit_tests: tuple[str, ...]
    integration_tests: tuple[str, ...]
    system_tests: tuple[str, ...]
    acceptance_tests: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    first_stage: EvidenceStage

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def validate_requirement_contract(contract: RequirementContract) -> list[str]:
    errors: list[str] = []
    if not contract.requirement_id.startswith("SW-"):
        errors.append("requirement_id must start with SW-")
    if not contract.command:
        errors.append("command is required")
    if not contract.code_modules:
        errors.append("at least one code module is required")
    if not contract.unit_tests:
        errors.append("at least one unit test is required")
    if not contract.evidence_ids:
        errors.append("at least one evidence id is required")
    return errors
