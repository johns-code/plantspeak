from __future__ import annotations

from dataclasses import asdict, dataclass

from plantspeak.devices import build_capability_map


@dataclass(frozen=True)
class ICDCapability:
    requirement_id: str
    command: str
    implementation_status: str
    verification_method: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


COMMANDS_BY_REQUIREMENT = {
    "SW-001": "describe-icd",
    "SW-002": "set-user-led",
    "SW-003": "read-user-button",
    "SW-004": "set-peripheral-enable",
    "SW-005": "scan-i2c-bus",
    "SW-006": "read-light-sensors",
    "SW-007": "drive-wavelength-leds",
    "SW-008": "read-leaf-temperature",
    "SW-009": "read-ambient-climate",
    "SW-010": "read-acceleration",
    "SW-011": "set-dev-board-led",
    "SW-012": "report-peripheral-enable-unavailable",
    "SW-013": "read-canned-sensor-data",
    "SW-014": "report-user-button-unavailable",
}


def build_icd_capabilities() -> list[ICDCapability]:
    capability_map = build_capability_map()
    capabilities: list[ICDCapability] = []
    for requirement_id, command in COMMANDS_BY_REQUIREMENT.items():
        status = capability_map[requirement_id]
        method = "unit-test-and-dev-mode-cli"
        if status == "dev-board-unavailable":
            method = "requirements-trace-and-target-hardware-deferred-test"
        capabilities.append(ICDCapability(requirement_id, command, status, method))
    return capabilities


def capability_summary() -> dict[str, dict[str, str]]:
    return {capability.requirement_id: capability.to_dict() for capability in build_icd_capabilities()}
