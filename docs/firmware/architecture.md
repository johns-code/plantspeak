# Firmware Architecture

Project: PlantSpeak

## Purpose

Define the DA14531 target firmware architecture that will eventually implement the PlantSpeak ICD while preserving the PC/dev-mode contracts already generated in the baseline.

## Firmware Layers

| Layer | Responsibility | Modules |
| --- | --- | --- |
| ICD command layer | Decode commands, validate payloads, route requests, encode responses. | `icd_command_table`, `icd_dispatch`, `icd_response`, `fault_codes` |
| Application services | Implement product behavior independent of transport and device drivers. | `measurement_service`, `led_sequence_service`, `self_test_service`, `power_service` |
| HAL | Isolate DA14531 SDK and board differences. | `hal_gpio`, `hal_i2c`, `hal_timer`, `hal_power`, `hal_storage`, `hal_transport` |
| Device drivers | Implement target-board peripheral access through HAL interfaces. | `ads1115_driver`, `pca9846_driver`, `lp5816_driver`, `mlx90632_driver`, `hdc2010_driver`, `mxc4005_driver` |
| Board support | Own pin map, board capability profile, dev-board substitutes, and target-board availability. | `board_pins`, `board_profile_devkit`, `board_profile_target` |
| Transport | Move ICD frames between PC/smart device and firmware. | `ble_transport`, `transport_frame`, `transport_security` |
| Diagnostics and V&V hooks | Provide test hooks, self-test, error evidence, and HIL observability. | `diagnostics`, `test_hooks`, `evidence_log` |

## Module Map

| Module | Inputs | Outputs | Requirements | First Stage |
| --- | --- | --- | --- | --- |
| `icd_dispatch` | BLE/local ICD command frame | typed response or `fault_code` | SW-001, SW-007 | S4 |
| `measurement_service` | measurement command, board profile | measurement response with source/status metadata | SW-006, SW-008, SW-009, SW-010, SW-013 | S3 |
| `led_sequence_service` | wavelength sequence request | LP5816/PCA9846 operations and settling events | SW-007 | S3 |
| `self_test_service` | self-test command | per-capability status map | SW-001, SW-011, SW-012, SW-013, SW-014 | S5 |
| `power_service` | sleep/wake command, P0_10 event | power transition status | SW-003, SW-014 | S6 |
| `hal_gpio` | pin operation | DA14531 GPIO write/read | SW-002, SW-003, SW-004 | S5 |
| `hal_i2c` | I2C transaction | status, bytes read/written, timeout/error | SW-005 | S5 |
| `ble_transport` | BLE GATT payload | ICD frame delivered to `icd_dispatch` | SW-001 | S4 |

## Firmware Interfaces

| Interface | Contract | Error Handling | Verification |
| --- | --- | --- | --- |
| ICD frame | command id, payload length, payload bytes, correlation id | malformed frame returns protocol fault and does not execute side effects | `tests/test_transport.py`, `tests/test_security_transport.py` |
| Measurement response | status, source, photodiode current, PPFD, leaf temp, ambient temp, RH, acceleration | missing device returns explicit device fault or dev-mode canned source | `tests/test_adapters.py`, ST-004, ST-006 |
| I2C transaction | bus id, address, write bytes, read length, timeout | timeout, NACK, invalid length, CRC/data validation fault | adapter error-path tests |
| Board profile | capability flags for devkit/target board | unavailable capability reports deferred/unavailable, never silent success | `tests/test_contracts.py`, HIL evidence |
| Evidence log | test id, requirement id, timestamp/source, status, fault code | failed operation emits evidence record before response | `tests/test_system_evidence.py` |

## Pin And Peripheral Ownership

| Signal / Device | Firmware Owner | Pin / Bus | Requirement | Verification Stage |
| --- | --- | --- | --- | --- |
| red user LED | `hal_gpio`, `board_pins` | P0_5 | SW-002 | S6 |
| green user LED | `hal_gpio`, `board_pins` | P0_11 | SW-002 | S6 |
| user push button | `power_service`, `hal_gpio` | P0_10 | SW-003, SW-014 | S6 |
| EN_Peripherals | `hal_gpio`, `board_pins` | P0_6 | SW-004, SW-012 | S6 |
| I2C SCL/SDA | `hal_i2c` | P0_8/P0_9 | SW-005 | S5/S6 |
| ADS1115 | `ads1115_driver` | DA14531 I2C | SW-006 | S3/S6 |
| PCA9846 | `pca9846_driver` | DA14531 I2C | SW-007, SW-008 | S3/S6 |
| LP5816 | `lp5816_driver` | PCA9846 channels SC1/SD1 and SC2/SD2 | SW-007 | S3/S6 |
| MLX90632 | `mlx90632_driver` | PCA9846 channel SC0/SD0 | SW-008 | S3/S6 |
| HDC2010 | `hdc2010_driver` | DA14531 I2C | SW-009 | S3/S6 |
| MXC4005XC | `mxc4005_driver` | DA14531 I2C | SW-010 | S3/S6 |

## Measurement Sequence

1. `icd_dispatch` receives a measurement command.
2. `measurement_service` checks board profile and EN_Peripherals availability.
3. Target mode enables P0_6 through `hal_gpio`; dev mode records unavailable/substituted evidence.
4. `led_sequence_service` selects PCA9846 channel and configures LP5816 LED intensity.
5. `hal_timer` applies settling delay defined by the detailed design stage.
6. `ads1115_driver` reads AIN0 for each wavelength and AIN1 for PPFD.
7. `mlx90632_driver`, `hdc2010_driver`, and `mxc4005_driver` collect environment and motion values.
8. `measurement_service` composes the response and `evidence_log` records requirement coverage.
9. `ble_transport` returns the ICD response.

## Mode Strategy

| Mode | Behavior |
| --- | --- |
| Dev-board mode | Uses board profile to mark unavailable LEDs, EN_Peripherals, push button wake, and external I2C devices. Canned providers preserve response shape. |
| Target-board mode | Uses real GPIO, I2C, PCA9846 mux, device drivers, BLE transport, and HIL evidence. |
| Test mode | Allows deterministic fault injection for missing I2C device, timeout, malformed BLE payload, and unavailable board capability. |

## Detailed Design Inputs

| Detailed Design Topic | Required Input From This Architecture |
| --- | --- |
| ICD command detailed design | command table, dispatch route, frame validation, response/fault model |
| HAL detailed design | GPIO/I2C/timer/power/transport function contracts and error returns |
| Driver detailed design | per-device init/read/write sequence, timeout behavior, and validation rules |
| Measurement detailed design | sequencing order, settling timing, units, calibration assumptions, evidence record |
| BLE detailed design | GATT service/characteristic plan, frame size, retry/timeout, malformed payload handling |
| HIL detailed design | test hooks, board setup, evidence file format, operator procedure |

## Firmware Verification Hooks

| Hook | Purpose | Stage |
| --- | --- | --- |
| `test_hooks_set_board_profile` | Select devkit/target/fault-injection capability profile. | S5 |
| `test_hooks_set_i2c_fault` | Inject NACK, timeout, invalid data, or missing device. | S3/S6 |
| `diagnostics_get_last_fault` | Read last firmware fault for test evidence. | S4/S6 |
| `evidence_log_export` | Export requirement-linked firmware evidence records. | S6 |

## Open Firmware Decisions

| Decision | Owner | Due Stage |
| --- | --- | --- |
| Exact BLE GATT service/characteristic UUIDs | firmware_development_agent, security_review_agent | S4 |
| DA14531 SDK/build invocation and CI feasibility | firmware_development_agent, release_quality_agent | S5 |
| Measurement settling delay and calibration constants | systems_architecture_agent, product_requirements_agent | S3 |
| HIL fixture and operator procedure | qa_verification_agent, firmware_development_agent | S6 |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
