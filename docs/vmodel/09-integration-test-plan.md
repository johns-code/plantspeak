# Integration Test Plan

Project: PlantSpeak

| Test ID | Requirements | Integration | Status | Evidence |
| --- | --- | --- | --- | --- |
| IT-001 | SW-001, SW-013 | CLI loads requirements, ICD capabilities, issue links, and dev-board profile. | Implemented | `tests/test_cli.py` |
| IT-002 | SW-006 through SW-010 | Dev-mode measurement integrates all canned sensor values in one snapshot. | Implemented | `tests/test_cli.py`, `tests/test_devices.py` |
| IT-003 | SW-002 through SW-005, SW-011 through SW-014 | Capability map integrates pin constraints and unavailable hardware decisions. | Implemented | `tests/test_devices.py`, `tests/test_icd.py` |
