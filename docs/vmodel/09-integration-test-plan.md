# Integration Test Plan

Project: PlantSpeak

## Integration Test Design Rule

Integration tests verify boundaries between components and stages. Each test names the setup, procedure, observable output, fault case, evidence artifact, and promotion gate.

| Test ID | Requirements | Integration Boundary | Fixture / Setup | Procedure | Expected Observability | Negative / Fault Case | Evidence | Promotion Gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IT-001 | SW-001, SW-013 | requirements package -> ICD capability catalog -> CLI | fresh checkout with packaged `requirements.json` and `issue_links.json` | run `python -m plantspeak.cli capabilities` and parse JSON | all 14 SW IDs appear with command, status, and verification method | delete or alter one requirement link; traceability gate must fail | `tests/test_cli.py`, `tests/test_icd.py`, ST-003 JSON | S1 contracts complete |
| IT-002 | SW-001, SW-002, SW-003, SW-004, SW-005, SW-011, SW-012, SW-014 | pin map -> dev-board profile -> capability map -> self-test | default dev-board profile fixture | run `python -m plantspeak.cli self-test --dev-mode` | JSON reports ICD present, external I2C canned, button wake deferred, unavailable hardware explicit | mark unavailable hardware as implemented; test must fail | `tests/test_devices.py`, `tests/test_icd.py`, ST-001 JSON | S2 dev-mode harness complete |
| IT-003 | SW-006, SW-008, SW-009, SW-010, SW-013 | measurement provider -> SensorSnapshot -> CLI JSON | deterministic dev-mode provider | run `python -m plantspeak.cli measure --dev-mode` | JSON contains all sensor fields, units implied by names, and `source=canned-dev-mode-data` | remove source metadata or one field; schema/CLI test must fail | `tests/test_cli.py`, `tests/test_devices.py`, ST-004 JSON | S2 measurement evidence stable |
| IT-004 | SW-005, SW-006, SW-007, SW-008, SW-009, SW-010, SW-013 | HAL I2C -> mux/device adapters -> measurement service | mocked I2C bus with success, missing device, timeout, and invalid-data scripts | run `python -m pytest tests/test_adapters.py` | adapters return typed values or explicit device faults without silent success | inject NACK, timeout, missing device, invalid data | `tests/test_adapters.py`, `docs/test-evidence/S3-pytest.txt` | S3 hardware adapter layer complete |
| IT-005 | SW-001, SW-007 | BLE/local transport -> ICD dispatch -> command response | mocked transport with valid, malformed, oversized, and timeout frames | run `python -m pytest tests/test_transport.py tests/test_security_transport.py` | valid command reaches dispatch; malformed payload returns protocol fault and no success side effects | malformed frame, timeout, unsupported command | `tests/test_transport.py`, `tests/test_security_transport.py`, `docs/test-evidence/S4-pytest.txt` | S4 mocked BLE/ICD transport contract complete |
| IT-006 | SW-001, SW-002, SW-003, SW-004, SW-005 | firmware command table -> pin config -> documented build path | DA14531 contract-only build fixture | run `python -m pytest tests/test_firmware_contracts.py` and inspect `firmware/build.ps1` | firmware command table and pin config match S1 contracts | missing toolchain, bad pin mapping, stale command ID | `tests/test_firmware_contracts.py`, `docs/test-evidence/S5-pytest.txt` | S5 firmware contract path complete |
| IT-007 | SW-002, SW-003, SW-004, SW-005, SW-006, SW-007, SW-008, SW-009, SW-010, SW-014 | target board -> firmware -> BLE/PC harness -> HIL evidence | target board, flashed firmware, external peripherals, operator checklist | run `python -m pytest tests/hil --target-board` or manual HIL procedure | LEDs, EN_Peripherals, I2C reads, measurement sequence, and wake behavior produce requirement-linked evidence | disconnect device, press wake incorrectly, corrupt measurement path | `docs/test-evidence/ST-006-hil-report.md` | S6 HIL qualification complete |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
