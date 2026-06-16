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

## Human Approval Gate

The branch can be reviewed and merged only after the human accepts the dev-mode scope and acknowledges that target-board hardware-in-loop evidence is deferred.
