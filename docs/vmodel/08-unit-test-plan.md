# Unit Test Plan

Project: PlantSpeak

## Unit Test Design Rule

Every unit test must identify the fixture/input, concrete assertions, a negative, edge, or fault case, and the stage gate it supports. A row that only says `python -m pytest` is not detailed test design.

| Test ID | Requirement | Unit Under Test | Fixture / Input | Assertions | Negative / Edge Case | Evidence | Stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UT-001 | SW-001 | plantspeak/icd.py | ICD catalog fixture with all requirement records | assert capability summary contains every SW ID, command, status, and verification method | remove one SW ID from fixture; test must fail coverage check | `python -m pytest`; named test module in RTM | S1 |
| UT-002 | SW-002 | plantspeak/pins.py, plantspeak/devices.py | pin map fixture | assert red and green LED signals resolve to P0_5/P0_11 and link SW-002 | duplicate or missing LED signal fails pin assignment test | `python -m pytest`; named test module in RTM | S1 |
| UT-003 | SW-003 | plantspeak/pins.py, plantspeak/devices.py | dev-board profile fixture | assert user push button maps to P0_10 and wake is unavailable/deferred | target-only wake cannot report implemented in dev profile | `python -m pytest`; named test module in RTM | S1 |
| UT-004 | SW-004 | plantspeak/pins.py, plantspeak/devices.py | dev-board profile fixture | assert EN_Peripherals maps to P0_6 and unavailable state is explicit | missing availability note fails capability map test | `python -m pytest`; named test module in RTM | S1 |
| UT-005 | SW-005 | plantspeak/pins.py, plantspeak/devices.py | pin map fixture | assert I2C SCL/SDA resolve to P0_8/P0_9 | swapped or missing I2C pins fail assignment test | `python -m pytest`; named test module in RTM | S1 |
| UT-006 | SW-006 | plantspeak/devices.py | dev-mode measurement fixture | assert photodiode current, PPFD, units, and source metadata are present | hardware-mode request before adapter returns unsupported/deferred | `python -m pytest`; named test module in RTM | S2 |
| UT-007 | SW-007 | plantspeak/icd.py, plantspeak/devices.py | ICD command fixture | assert drive-wavelength-leds capability exists with target-adapter status | missing command blocks S3 adapter promotion | `python -m pytest`; named test module in RTM | S2 |
| UT-008 | SW-008 | plantspeak/devices.py | dev-mode measurement fixture | assert leaf temperature field and source metadata are present | missing sensor field fails snapshot contract | `python -m pytest`; named test module in RTM | S2 |
| UT-009 | SW-009 | plantspeak/devices.py | dev-mode measurement fixture | assert ambient temperature and relative humidity fields are present | invalid humidity range fails snapshot validation | `python -m pytest`; named test module in RTM | S2 |
| UT-010 | SW-010 | plantspeak/devices.py | dev-mode measurement fixture | assert acceleration_g is a three-value vector | wrong vector length fails snapshot validation | `python -m pytest`; named test module in RTM | S2 |
| UT-011 | SW-011 | plantspeak/devices.py | capability map fixture | assert LED substitute behavior is marked dev-board substitute | substitute cannot be reported as target hardware success | `python -m pytest`; named test module in RTM | S2 |
| UT-012 | SW-012 | plantspeak/devices.py | capability map fixture | assert EN_Peripherals unavailable status is visible | silent success for unavailable hardware fails test | `python -m pytest`; named test module in RTM | S2 |
| UT-013 | SW-013 | plantspeak/devices.py | measurement provider fixture | assert canned-dev-mode-data source metadata is emitted | missing source metadata blocks verification evidence | `python -m pytest`; named test module in RTM | S2 |
| UT-014 | SW-014 | plantspeak/devices.py, plantspeak/icd.py | ICD and profile fixture | assert wake behavior is deferred/unavailable in capability summary | wake cannot be marked implemented without HIL evidence | `python -m pytest`; named test module in RTM | S2 |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
