# Detailed Design Notes

Project: PlantSpeak

## ICD Capability Model

`plantspeak.icd` maps each software requirement to one command, an implementation status, and a verification method. This prevents vague implementation claims: every ICD behavior has an inspectable status such as `modeled`, `canned-data`, `dev-board-led-substitute`, or `dev-board-unavailable`.

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

| Condition | Dev-Mode Behavior | Target Stage |
| --- | --- | --- |
| External I2C unavailable | Return canned data and mark source `canned-dev-mode-data`. | S3/S6 |
| User push button unavailable | Capability reports `dev-board-unavailable`. | S6 |
| Hardware mode requested before adapter exists | CLI exits with explicit unsupported-mode message. | S3-S5 |

## Command Surface

| Command | Purpose |
| --- | --- |
| `list-requirements` | Show packaged software requirements. |
| `trace` | Show requirement, issue, command, and verification mapping. |
| `capabilities` | Emit ICD capability summary as JSON. |
| `measure --dev-mode` | Emit canned sensor snapshot. |
| `self-test --dev-mode` | Run deterministic dev-board checks. |

## Deferred Design Items

- DA14531 firmware build, flash, and hardware execution flow.
- BLE transport implementation between PC test harness and target firmware.
- Wake-from-sleep behavior requiring the unavailable user push button or final target hardware.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
