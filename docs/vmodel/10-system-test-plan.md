# System Test Plan

Project: PlantSpeak

| Test ID | Scenario | Requirements | Status | Evidence |
| --- | --- | --- | --- | --- |
| ST-001 | Run `python -m plantspeak.cli self-test --dev-mode` and require all checks true. | SW-001 through SW-014 | Implemented | PR CI plus local report |
| ST-002 | Run `python -m plantspeak.cli trace` and verify requirement-to-issue-to-command trace rows. | SW-001 through SW-014 | Implemented | CLI tests |
| ST-003 | Run target-board hardware-in-loop test after final hardware is available. | SW-002 through SW-010, SW-014 | Deferred | Human-approved deferred evidence |
