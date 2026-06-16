# ST-006 Hardware-In-Loop Report

Status: Deferred - target board not connected in this CI run.

## Required Setup

- DA14531 target board with PlantSpeak firmware image.
- External I2C peripherals populated according to the schematic.
- PC transport path connected to the target.
- Operator sets `PLANTSPEAK_TARGET_BOARD=1`.

## Required Procedure

```powershell
python -m pytest tests/hil --target-board
```

## Required Evidence

| Check | Requirement Coverage | Evidence |
| --- | --- | --- |
| LEDs and EN_Peripherals | SW-002, SW-004, SW-012 | Captured GPIO/HIL log |
| External I2C measurement sequence | SW-005, SW-006, SW-007, SW-008, SW-009, SW-010 | Captured measurement and device logs |
| Push-button wake | SW-003, SW-014 | Captured wake/sleep transition log |

## Current Disposition

S6 infrastructure exists, but final HIL qualification remains blocked until physical target-board access is provided.
