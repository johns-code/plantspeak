# Software Requirements Specification

Project: PlantSpeak

| ID | Module | Observable Behavior | Verification Test |
| --- | --- | --- | --- |
| SW-001 | plantspeak.icd | `capabilities` prints JSON object with 14 requirement keys. | tests/test_icd.py::test_icd_capabilities_cover_all_software_requirements |
| SW-002 | plantspeak.pins | Pin map exposes red_user_led=P0_5 and green_user_led=P0_11. | tests/test_devices.py::test_pin_assignments_match_requirements |
| SW-003 | plantspeak.pins | Pin map exposes user_push_button=P0_10 and capability status is dev-board-unavailable. | tests/test_devices.py::test_capability_map_marks_deferred_hardware |
| SW-004 | plantspeak.pins | Pin map exposes en_peripherals=P0_6 and capability status is dev-board-unavailable. | tests/test_devices.py::test_capability_map_marks_deferred_hardware |
| SW-005 | plantspeak.pins | Pin map exposes i2c_scl=P0_8 and i2c_sda=P0_9. | tests/test_devices.py::test_pin_assignments_match_requirements |
| SW-006 | plantspeak.devices | `measure --dev-mode` emits photodiode current and PPFD fields. | tests/test_cli.py::test_measure_dev_mode_outputs_canned_snapshot |
| SW-007 | plantspeak.icd | Capability map includes command `drive-wavelength-leds` and marks target adapter work. | tests/test_icd.py |
| SW-008 | plantspeak.devices | `measure --dev-mode` emits `leaf_temperature_c`. | tests/test_cli.py |
| SW-009 | plantspeak.devices | `measure --dev-mode` emits ambient temperature and RH fields. | tests/test_cli.py |
| SW-010 | plantspeak.devices | `measure --dev-mode` emits `acceleration_g` list. | tests/test_devices.py::test_canned_sensor_snapshot_supports_dev_mode |
| SW-011 | plantspeak.devices | Capability map marks LED work as dev-board substitute. | tests/test_devices.py |
| SW-012 | plantspeak.devices | Capability map marks EN_Peripherals unavailable. | tests/test_devices.py |
| SW-013 | plantspeak.devices | Measurement source is canned dev-mode data. | tests/test_devices.py::test_canned_sensor_snapshot_supports_dev_mode |
| SW-014 | plantspeak.icd | Capability map and ICD summary mark user-button wake unavailable/deferred. | tests/test_icd.py::test_icd_summary_identifies_deferred_wake_behavior |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
