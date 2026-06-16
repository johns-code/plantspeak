# Requirements Traceability Matrix

Project: PlantSpeak

## S1 Traceability Rule

The authoritative trace source is `plantspeak.trace.build_requirement_contracts()`. The `trace-json` CLI command validates requirement IDs, issue links, ICD commands, code modules, test references, evidence IDs, and first implementation stage before emitting JSON.

| Requirement | Issue | Command | Code | Tests | Evidence | First Stage | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SW-001 | #114 | `describe-icd` | `plantspeak/icd.py`, `plantspeak/cli.py` | `tests/test_icd.py`, IT-001, IT-002, ST-001, ST-002, ST-003, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S1 | modeled |
| SW-002 | #115 | `set-user-led` | `plantspeak/pins.py`, `plantspeak/devices.py` | `tests/test_devices.py`, IT-002, ST-002, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S1 | dev-board-led-substitute |
| SW-003 | #116 | `read-user-button` | `plantspeak/pins.py`, `plantspeak/devices.py` | `tests/test_devices.py`, IT-002, ST-002, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S1 | dev-board-unavailable |
| SW-004 | #117 | `set-peripheral-enable` | `plantspeak/pins.py`, `plantspeak/devices.py` | `tests/test_devices.py`, IT-002, ST-002, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S1 | dev-board-unavailable |
| SW-005 | #118 | `scan-i2c-bus` | `plantspeak/pins.py`, `plantspeak/devices.py` | `tests/test_devices.py`, IT-002, IT-004, ST-002, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S1 | dev-board-unavailable |
| SW-006 | #119 | `read-light-sensors` | `plantspeak/devices.py`, `plantspeak/cli.py` | `tests/test_cli.py`, IT-003, IT-004, ST-004, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | canned-data |
| SW-007 | #120 | `drive-wavelength-leds` | `plantspeak/icd.py`, `plantspeak/devices.py` | `tests/test_icd.py`, IT-004, IT-005, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | canned-data |
| SW-008 | #121 | `read-leaf-temperature` | `plantspeak/devices.py`, `plantspeak/cli.py` | `tests/test_cli.py`, IT-003, IT-004, ST-004, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | canned-data |
| SW-009 | #122 | `read-ambient-climate` | `plantspeak/devices.py`, `plantspeak/cli.py` | `tests/test_cli.py`, IT-003, IT-004, ST-004, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | canned-data |
| SW-010 | #123 | `read-acceleration` | `plantspeak/devices.py`, `plantspeak/cli.py` | `tests/test_devices.py`, IT-003, IT-004, ST-004, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | canned-data |
| SW-011 | #124 | `set-dev-board-led` | `plantspeak/devices.py`, `plantspeak/pins.py` | `tests/test_devices.py`, IT-002, ST-001, ST-002, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | dev-board-led-substitute |
| SW-012 | #125 | `report-peripheral-enable-unavailable` | `plantspeak/devices.py`, `plantspeak/pins.py` | `tests/test_devices.py`, IT-002, ST-002, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | dev-board-unavailable |
| SW-013 | #126 | `read-canned-sensor-data` | `plantspeak/devices.py`, `plantspeak/cli.py` | `tests/test_devices.py`, IT-001, IT-003, ST-001, ST-004, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | canned-data |
| SW-014 | #127 | `report-user-button-unavailable` | `plantspeak/icd.py`, `plantspeak/devices.py` | `tests/test_icd.py`, IT-002, IT-007, ST-001, ST-006, AT-001..AT-004 | `docs/test-evidence/S1-trace-matrix.json` | S2 | dev-board-unavailable |

## Mechanical Checks

| Check | Evidence |
| --- | --- |
| No dangling requirement IDs | `tests/test_traceability.py::test_trace_matrix_has_no_dangling_requirement_links` |
| Every trace row has code, tests, and evidence | `tests/test_traceability.py::test_trace_rows_link_requirements_to_code_tests_and_evidence` |
| Contract rows validate required fields | `tests/test_contracts.py::test_requirement_contracts_are_complete` |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed by making `plantspeak.trace` the mechanical source of trace truth and by replacing placeholder test IDs with real planned or implemented evidence. |
| Staged implementation readiness | S1 now defines contract and trace APIs that later stages must preserve. |
| Software Lead disposition | Cleared for S1 branch review, subject to CI and PR review. |
