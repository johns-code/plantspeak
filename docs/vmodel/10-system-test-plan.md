# System Test Plan

Project: PlantSpeak

## Scope Rule

System tests may only claim behavior they execute. Dev-mode tests prove PC harness behavior, contract shape, traceability, and explicit fallback/deferred statuses. They do not prove target-board I2C, BLE transport, DA14531 firmware execution, EN_Peripherals control, or push-button wake behavior.

| ID | Test | Preconditions | Command / Procedure | Expected Result | Evidence Artifact | Requirements | Limits | Failure Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-001 | Dev-mode self-test | Fresh checkout; package installed with `python -m pip install -e .[dev]`. | `python -m plantspeak.cli generate-evidence --output-dir docs/test-evidence/s2-devmode` | Exit code 0; `ST-001.json` has `external_i2c_uses_canned_data=true`, `button_wake_deferred=true`, `icd_capabilities_present=true`. | `docs/test-evidence/s2-devmode/ST-001.json`; GitHub Actions `test` log | SW-001, SW-013, SW-014 | Does not prove real I2C, BLE, firmware, EN_Peripherals, or target-board push-button wake. | Create or update a GitHub issue linked to failed requirement and block promotion from S2. |
| ST-002 | Requirement trace output | Fresh checkout; generated `plantspeak/data/issue_links.json` exists. | `python -m plantspeak.cli generate-evidence --output-dir docs/test-evidence/s2-devmode` | Output contains one trace row for each software requirement with issue number, command, and verification method. | `docs/test-evidence/s2-devmode/ST-002.txt`; CI captured stdout | SW-001, SW-002, SW-003, SW-004, SW-005, SW-006, SW-007, SW-008, SW-009, SW-010, SW-011, SW-012, SW-013, SW-014 as trace records only | Does not prove hardware execution; proves inspectable traceability only. | Create or update a GitHub issue for missing/incorrect trace row and block RTM closure. |
| ST-003 | ICD capability summary | Fresh checkout; package installed. | `python -m plantspeak.cli generate-evidence --output-dir docs/test-evidence/s2-devmode` | Valid JSON object with 14 keys; SW-006/SW-013 statuses are `canned-data`; SW-014 is `dev-board-unavailable`; SW-001 command is `describe-icd`. | `docs/test-evidence/s2-devmode/ST-003.json`; JSON validation in pytest | SW-001, SW-006, SW-013, SW-014 | Does not prove target command transport; proves local ICD contract shape. | Create or update a GitHub issue and block S4 BLE/ICD transport entry. |
| ST-004 | Dev-mode measurement output | Fresh checkout; no external I2C devices required. | `python -m plantspeak.cli generate-evidence --output-dir docs/test-evidence/s2-devmode` | Exit code 0; JSON contains `photodiode_current_ua`, `ppfd_umol_m2_s`, `leaf_temperature_c`, `ambient_temperature_c`, `relative_humidity_percent`, `acceleration_g`, and `source=canned-dev-mode-data`. | `docs/test-evidence/s2-devmode/ST-004.json`; CLI test log | SW-006, SW-008, SW-009, SW-010, SW-013 | Does not prove ADS1115, LP5816/PCA9846, MLX90632, HDC2010, or MXC4005XC hardware reads. | Create or update a GitHub issue and block S3 hardware adapter promotion. |
| ST-005 | Fresh checkout CI system gate | GitHub PR branch pushed; CI workflow present. | GitHub Actions workflow `CI` job `test` runs `python -m pip install -e .[dev]` and `python -m pytest`. | Workflow conclusion is success for the PR head SHA. | GitHub Actions run URL in PR checks; `docs/reviews/test-report.md` | SW-001, SW-002, SW-003, SW-004, SW-005, SW-006, SW-007, SW-008, SW-009, SW-010, SW-011, SW-012, SW-013, SW-014 as implemented dev-mode test scope | Does not prove manual user acceptance or target-board evidence. | Keep PR unmerged and create/update issue for failing test or environment defect. |
| ST-006 | Target-board HIL qualification | Target board, DA14531 firmware, BLE transport, and external peripherals available. | Run `python -m pytest tests/hil --target-board` with `PLANTSPEAK_TARGET_BOARD=1`. | LEDs, EN_Peripherals, I2C devices, measurement sequence, and push-button wake pass requirement-specific checks. | `docs/test-evidence/ST-006-hil-report.md`; `docs/test-evidence/hil-operator-notes.md` | SW-002, SW-003, SW-004, SW-005, SW-006, SW-007, SW-008, SW-009, SW-010, SW-014 | Deferred until target hardware and firmware transport exist; skipped in normal CI. | Create or update hardware qualification issues and keep final release blocked. |

## Promotion Criteria

- S2 may proceed when ST-001, ST-002, ST-003, ST-004, and ST-005 pass on the PR branch.
- S3 may proceed only after ST-004 evidence is stable and hardware adapter contracts are reviewed.
- S4 may proceed only after ST-003 contract evidence is stable.
- S6 cannot be claimed complete until ST-006 has real hardware-in-loop evidence.

## Defect Rule

Any failed system test must create or update a GitHub issue linked to the affected requirement, attach the failing evidence artifact or CI URL, and block the next stage gate until resolved or explicitly deferred by the Software Lead and human approver.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
