from __future__ import annotations

from plantspeak.contracts import RequirementContract, validate_requirement_contract
from plantspeak.icd import COMMANDS_BY_REQUIREMENT
from plantspeak.requirements import load_issue_links, load_requirements


CODE_BY_REQUIREMENT = {
    "SW-001": ("plantspeak/icd.py", "plantspeak/cli.py"),
    "SW-002": ("plantspeak/pins.py", "plantspeak/devices.py"),
    "SW-003": ("plantspeak/pins.py", "plantspeak/devices.py"),
    "SW-004": ("plantspeak/pins.py", "plantspeak/devices.py"),
    "SW-005": ("plantspeak/pins.py", "plantspeak/devices.py"),
    "SW-006": ("plantspeak/devices.py", "plantspeak/cli.py"),
    "SW-007": ("plantspeak/icd.py", "plantspeak/devices.py"),
    "SW-008": ("plantspeak/devices.py", "plantspeak/cli.py"),
    "SW-009": ("plantspeak/devices.py", "plantspeak/cli.py"),
    "SW-010": ("plantspeak/devices.py", "plantspeak/cli.py"),
    "SW-011": ("plantspeak/devices.py", "plantspeak/pins.py"),
    "SW-012": ("plantspeak/devices.py", "plantspeak/pins.py"),
    "SW-013": ("plantspeak/devices.py", "plantspeak/cli.py"),
    "SW-014": ("plantspeak/icd.py", "plantspeak/devices.py"),
}

UNIT_TEST_BY_REQUIREMENT = {
    "SW-001": ("tests/test_icd.py::test_icd_capabilities_cover_all_software_requirements",),
    "SW-002": ("tests/test_devices.py::test_pin_assignments_match_requirements",),
    "SW-003": ("tests/test_devices.py::test_capability_map_marks_deferred_hardware",),
    "SW-004": ("tests/test_devices.py::test_capability_map_marks_deferred_hardware",),
    "SW-005": ("tests/test_devices.py::test_pin_assignments_match_requirements",),
    "SW-006": ("tests/test_cli.py::test_measure_dev_mode_outputs_canned_snapshot",),
    "SW-007": ("tests/test_icd.py::test_icd_capabilities_cover_all_software_requirements",),
    "SW-008": ("tests/test_cli.py::test_measure_dev_mode_outputs_canned_snapshot",),
    "SW-009": ("tests/test_cli.py::test_measure_dev_mode_outputs_canned_snapshot",),
    "SW-010": ("tests/test_devices.py::test_canned_sensor_snapshot_supports_dev_mode",),
    "SW-011": ("tests/test_devices.py::test_capability_map_marks_deferred_hardware",),
    "SW-012": ("tests/test_devices.py::test_capability_map_marks_deferred_hardware",),
    "SW-013": ("tests/test_devices.py::test_canned_sensor_snapshot_supports_dev_mode",),
    "SW-014": ("tests/test_icd.py::test_icd_summary_identifies_deferred_wake_behavior",),
}

INTEGRATION_TEST_BY_REQUIREMENT = {
    "SW-001": ("IT-001", "IT-002"),
    "SW-002": ("IT-002",),
    "SW-003": ("IT-002",),
    "SW-004": ("IT-002",),
    "SW-005": ("IT-002", "IT-004"),
    "SW-006": ("IT-003", "IT-004"),
    "SW-007": ("IT-004", "IT-005"),
    "SW-008": ("IT-003", "IT-004"),
    "SW-009": ("IT-003", "IT-004"),
    "SW-010": ("IT-003", "IT-004"),
    "SW-011": ("IT-002",),
    "SW-012": ("IT-002",),
    "SW-013": ("IT-001", "IT-003"),
    "SW-014": ("IT-002", "IT-007"),
}

SYSTEM_TEST_BY_REQUIREMENT = {
    "SW-001": ("ST-001", "ST-002", "ST-003"),
    "SW-002": ("ST-002", "ST-006"),
    "SW-003": ("ST-002", "ST-006"),
    "SW-004": ("ST-002", "ST-006"),
    "SW-005": ("ST-002", "ST-006"),
    "SW-006": ("ST-004", "ST-006"),
    "SW-007": ("ST-006",),
    "SW-008": ("ST-004", "ST-006"),
    "SW-009": ("ST-004", "ST-006"),
    "SW-010": ("ST-004", "ST-006"),
    "SW-011": ("ST-001", "ST-002"),
    "SW-012": ("ST-002", "ST-006"),
    "SW-013": ("ST-001", "ST-004"),
    "SW-014": ("ST-001", "ST-006"),
}

ACCEPTANCE_TEST_BY_REQUIREMENT = {
    requirement_id: ("AT-001", "AT-002", "AT-003", "AT-004") for requirement_id in CODE_BY_REQUIREMENT
}

FIRST_STAGE_BY_REQUIREMENT = {
    "SW-001": "S1",
    "SW-002": "S1",
    "SW-003": "S1",
    "SW-004": "S1",
    "SW-005": "S1",
    "SW-006": "S2",
    "SW-007": "S2",
    "SW-008": "S2",
    "SW-009": "S2",
    "SW-010": "S2",
    "SW-011": "S2",
    "SW-012": "S2",
    "SW-013": "S2",
    "SW-014": "S2",
}


def build_requirement_contracts() -> list[RequirementContract]:
    issues = {issue["requirement_ids"][0]: issue for issue in load_issue_links()}
    requirements = load_requirements()
    contracts: list[RequirementContract] = []
    for requirement in requirements:
        requirement_id = str(requirement["id"])
        issue = issues.get(requirement_id, {})
        contracts.append(
            RequirementContract(
                requirement_id=requirement_id,
                issue_number=issue.get("number"),
                command=COMMANDS_BY_REQUIREMENT[requirement_id],
                status=_status_for_requirement(requirement_id),
                code_modules=CODE_BY_REQUIREMENT[requirement_id],
                unit_tests=UNIT_TEST_BY_REQUIREMENT[requirement_id],
                integration_tests=INTEGRATION_TEST_BY_REQUIREMENT[requirement_id],
                system_tests=SYSTEM_TEST_BY_REQUIREMENT[requirement_id],
                acceptance_tests=ACCEPTANCE_TEST_BY_REQUIREMENT[requirement_id],
                evidence_ids=_evidence_ids(requirement_id),
                first_stage=FIRST_STAGE_BY_REQUIREMENT[requirement_id],
            )
        )
    return contracts


def trace_matrix() -> list[dict[str, object]]:
    return [contract.to_dict() for contract in build_requirement_contracts()]


def validate_trace_matrix() -> list[str]:
    requirement_ids = {str(requirement["id"]) for requirement in load_requirements()}
    issue_requirement_ids = {issue["requirement_ids"][0] for issue in load_issue_links()}
    command_ids = set(COMMANDS_BY_REQUIREMENT)
    errors: list[str] = []
    if requirement_ids != issue_requirement_ids:
        errors.append("requirement ids and issue requirement ids do not match")
    if requirement_ids != command_ids:
        errors.append("requirement ids and ICD command ids do not match")
    for contract in build_requirement_contracts():
        errors.extend(f"{contract.requirement_id}: {error}" for error in validate_requirement_contract(contract))
    return errors


def _status_for_requirement(requirement_id: str) -> str:
    from plantspeak.devices import build_capability_map

    return build_capability_map()[requirement_id]


def _evidence_ids(requirement_id: str) -> tuple[str, ...]:
    return (
        *UNIT_TEST_BY_REQUIREMENT[requirement_id],
        *INTEGRATION_TEST_BY_REQUIREMENT[requirement_id],
        *SYSTEM_TEST_BY_REQUIREMENT[requirement_id],
        *ACCEPTANCE_TEST_BY_REQUIREMENT[requirement_id],
    )
