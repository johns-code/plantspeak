# System Requirements Specification

Project: PlantSpeak

| ID | Priority | Requirement | Acceptance Criteria |
| --- | --- | --- | --- |
| SYS-001 | must | Expose an ICD capability summary for all PlantSpeak software requirements. | Capabilities JSON contains SW-001 through SW-014 with command, status, and verification method. |
| SYS-002 | must | Represent red and green user LEDs on P0_5 and P0_11. | Pin map contains both LED signals and dev-board substitute status. |
| SYS-003 | must | Represent user push button on P0_10. | Capability map marks push-button wake behavior unavailable on dev board and deferred for target board. |
| SYS-004 | must | Represent EN_Peripherals on P0_6. | Capability map marks EN_Peripherals unavailable on dev board and target-intended. |
| SYS-005 | must | Represent DA14531 I2C SCL P0_8 and SDA P0_9. | Pin map and trace output link I2C pins to SW-005. |
| SYS-006 | must | Support photodiode current and PPFD readings in dev mode. | Measurement snapshot includes `photodiode_current_ua` and `ppfd_umol_m2_s`. |
| SYS-007 | should | Model wavelength LED drive capability and PCA9846/LP5816 topology. | ICD command map includes `drive-wavelength-leds`; detailed design marks target adapter work. |
| SYS-008 | should | Support leaf temperature reading model. | Measurement snapshot includes `leaf_temperature_c`. |
| SYS-009 | should | Support RH and ambient temperature reading model. | Measurement snapshot includes `relative_humidity_percent` and `ambient_temperature_c`. |
| SYS-010 | should | Support accelerometer reading model. | Measurement snapshot includes `acceleration_g`. |
| SYS-011 | must | Use dev-board LED substitute for unavailable red/green LEDs. | Capability map marks SW-011 `dev-board-led-substitute`. |
| SYS-012 | must | Handle unavailable EN_Peripherals on dev board explicitly. | Capability map marks SW-012 `dev-board-unavailable`. |
| SYS-013 | must | Use canned data when external I2C devices are unavailable. | Measurement source is `canned-dev-mode-data`. |
| SYS-014 | must | Handle unavailable user push button explicitly. | Capability map marks SW-014 `dev-board-unavailable`. |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
