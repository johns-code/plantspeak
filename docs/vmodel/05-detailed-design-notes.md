# Detailed Design Notes

Project: PlantSpeak

## Design Scope And Stage Boundary

This detailed design covers the S0/S1 PC dev-mode contract and the detailed inputs that later S3-S6 target-board work must preserve. S0 proves inspectable command behavior, traceability, and deterministic canned evidence. S3-S6 must not change command names, response field names, requirement IDs, or evidence schemas without updating this document, the RTM, and the affected tests.

## ICD Capability Model

`plantspeak.icd` maps each software requirement to one command, an implementation status, and a verification method. This prevents vague implementation claims: every ICD behavior has an inspectable status such as `modeled`, `canned-data`, `dev-board-led-substitute`, or `dev-board-unavailable`.

## Component Contracts

| Component | Public Entry Points | Inputs | Outputs | Invariants | Error Contract |
| --- | --- | --- | --- | --- | --- |
| `plantspeak.requirements` | `load_requirements`, `load_issue_links`, `requirement_ids` | packaged JSON resources | ordered requirement records and issue links | every record has `SW-###`, statement, priority, acceptance criteria | invalid/missing packaged data fails tests before release |
| `plantspeak.icd` | `build_icd_capabilities`, `capability_summary` | requirement IDs, capability map | JSON-serializable command/status map | one capability record per software requirement | unknown requirement cannot silently disappear from summary |
| `plantspeak.pins` | `pin_map` | none | signal-to-pin records with requirement IDs | target pin assignments are centralized | conflicting/duplicate signals fail unit tests |
| `plantspeak.devices` | `default_dev_board_profile`, `build_capability_map`, `collect_dev_mode_snapshot` | board profile and dev-mode flag | capability statuses and sensor snapshot | unavailable target hardware is explicit, not reported as real success | unsupported hardware mode returns explicit unavailable/deferred status |
| `plantspeak.cli` | `main` | command argv | stdout JSON/text and process status | commands are deterministic in dev mode | unsupported commands/modes fail closed with nonzero status |

## Hardware Abstraction

`plantspeak.pins` records P0_5, P0_11, P0_10, P0_6, P0_8, and P0_9 as explicit assignments. `plantspeak.devices` separates dev-board availability from target-board intent, allowing tests to verify substitutions without pretending target hardware exists.

## Measurement Design

Dev mode returns a deterministic sensor snapshot for photodiode current, PPFD, leaf temperature, ambient temperature, relative humidity, and acceleration. Later target-board adapters should preserve the same snapshot shape while replacing canned data with ADS1115, LP5816/PCA9846, MLX90632, HDC2010, and MXC4005XC reads.

## Data Contracts

| Field | Unit | Dev-Mode Value | Source Requirement |
| --- | --- | --- | --- |
| `photodiode_current_ua` | microamps | 12.5 | SW-006 |
| `ppfd_umol_m2_s` | micromol/m2/s | 245.0 | SW-006 |
| `leaf_temperature_c` | Celsius | 24.2 | SW-008 |
| `ambient_temperature_c` | Celsius | 23.6 | SW-009 |
| `relative_humidity_percent` | percent | 51.0 | SW-009 |
| `acceleration_g` | g vector | `[0.01, -0.02, 1.0]` | SW-010 |

## Error And Deferred Behavior

| Condition | Detection Point | Dev-Mode Behavior | Target Stage | Required Test Design |
| --- | --- | --- | --- | --- |
| External I2C unavailable | `build_capability_map`, measurement provider | Return canned data and mark source `canned-dev-mode-data`. | S3/S6 | Unit test source metadata; integration test missing-device fault path. |
| User push button unavailable | board profile | Capability reports `dev-board-unavailable`. | S6 | Unit test capability map; HIL test proves wake only on target hardware. |
| Hardware mode requested before adapter exists | CLI/adapters | CLI exits with explicit unsupported-mode message. | S3-S5 | CLI negative test and stage gate before target claims. |
| Malformed command/transport payload | future `ble_transport` and `icd_dispatch` | Local harness rejects unsupported command; target path returns protocol fault. | S4 | Transport test with malformed frame and no side effects. |
| Device timeout or invalid data | future adapter HAL | Response contains explicit fault/status metadata and evidence record. | S3/S6 | Adapter test injects timeout/NACK/invalid data. |

## Command Surface

| Command | Inputs | Output Contract | Requirement Coverage | Negative Behavior |
| --- | --- | --- | --- | --- |
| `list-requirements` | none | one line per packaged SW requirement | SW-001 through SW-014 trace support | missing packaged data fails tests |
| `trace` | issue links and ICD map | requirement, issue, command, verification mapping | all SW requirements | missing issue link fails traceability gate |
| `capabilities` | ICD catalog and capability map | JSON object keyed by requirement ID | SW-001, SW-007, SW-014 | missing/deferred capabilities remain visible with status |
| `measure --dev-mode` | dev board profile | JSON snapshot with source metadata and fixed fields | SW-006, SW-008, SW-009, SW-010, SW-013 | non-dev hardware mode is unsupported until adapters exist |
| `self-test --dev-mode` | dev board profile and ICD map | JSON booleans for external I2C, wake deferral, ICD presence | SW-001, SW-013, SW-014 | false checks block S2 promotion |

## Detailed Design To Detailed Test Mapping

| Design Decision | Unit Tests | Integration Tests | System / Acceptance Evidence |
| --- | --- | --- | --- |
| Requirement records are packaged and stable | `tests/test_requirements.py` validates IDs and acceptance criteria | `tests/test_cli.py` exercises list/trace loading | ST-002 trace evidence |
| ICD capabilities never disappear | `tests/test_icd.py` validates all SW IDs and statuses | CLI capabilities JSON parsing | ST-003 capabilities artifact |
| Dev-board unavailable hardware is explicit | `tests/test_devices.py` validates profile and capability statuses | self-test integrates profile and ICD map | ST-001 self-test artifact |
| Measurement response shape is stable | `tests/test_devices.py` validates `SensorSnapshot.to_dict()` | CLI measure command emits full JSON | ST-004 measurement artifact |
| Future adapters preserve contracts | S3 adapter contract tests with fault injection | S3/S4 integration tests for adapters and transport | ST-006 HIL evidence |

## Deferred Design Items

- DA14531 firmware build, flash, and hardware execution flow.
- BLE transport implementation between PC test harness and target firmware.
- Wake-from-sleep behavior requiring the unavailable user push button or final target hardware.
- Exact target-board timing, calibration, settling delay, and HIL fixture procedure remain open decisions and must be resolved before S3/S6 closure.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
