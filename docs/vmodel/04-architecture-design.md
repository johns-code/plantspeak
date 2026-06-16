# Architecture/Design Document

Project: PlantSpeak

## Purpose

PlantSpeak will implement DA14531 ICD-facing capabilities while supporting a dev-board mode where unavailable target-board hardware is represented by deterministic substitutes and canned data.

## Architectural Drivers

| Driver | Decision |
| --- | --- |
| DA14531 ICD behavior | Model all ICD capabilities as explicit commands in `plantspeak.icd`. |
| Dev-board constraints | Keep target hardware intent while routing missing external I2C devices to canned data. |
| Hardware traceability | Centralize pins and availability in `plantspeak.pins` and `plantspeak.devices`. |
| Verification | Treat local pytest and GitHub Actions as deterministic gates. |
| Future firmware work | Keep Python harness boundaries clean so DA14531 firmware/BLE adapters can be added without rewriting tests. |

## Components

| Component | Responsibility | Requirements |
| --- | --- | --- |
| `plantspeak.cli` | User/test entry point for capabilities, trace, measurement, and self-test commands. | SW-001, SW-013 |
| `plantspeak.icd` | ICD command catalog and capability status map. | SW-001, SW-007, SW-014 |
| `plantspeak.pins` | DA14531 signal-to-pin assignments and dev-board availability notes. | SW-002, SW-003, SW-004, SW-005 |
| `plantspeak.devices` | Dev-board profile, canned sensor snapshot, capability status, and unavailable hardware decisions. | SW-006 through SW-014 |
| `plantspeak.data` | Requirements and GitHub issue traceability bundled with the package. | All |
| `tests/` | Deterministic unit and behavior checks used by local and CI gates. | All |

## Interface Contracts

| Interface | Current Contract | Future Adapter |
| --- | --- | --- |
| ICD command catalog | `plantspeak.icd.COMMANDS_BY_REQUIREMENT` maps SW IDs to command names and maturity. | Firmware command table and BLE command IDs in S4/S5. |
| Measurement snapshot | `SensorSnapshot.to_dict()` emits stable JSON fields and units. | ADS1115, LP5816/PCA9846, MLX90632, HDC2010, MXC4005XC adapters fill the same shape in S3/S6. |
| Pin/device registry | `PIN_ASSIGNMENTS` and `DevBoardProfile` separate target intent from dev-board availability. | DA14531 firmware pin configuration in S5. |
| PC harness transport | CLI currently executes local dev-mode commands. | BLE transport adapter introduced in S4 with malformed-payload tests. |

## Human Approval Gate

The branch can be reviewed and merged only after the human accepts the dev-mode scope and acknowledges that target-board hardware-in-loop evidence is deferred.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
