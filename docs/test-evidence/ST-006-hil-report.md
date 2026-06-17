# ST-006 Hardware-In-Loop Report

Status: Partially executed - local DA14531 build and non-invasive J-Link probe passed; full target-board HIL remains deferred.

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
| DA14531 Keil build | SW-001 through SW-014 firmware baseline | `keil-da14531-build-summary.json`, `keil-da14531-build-raw.log` |
| J-Link emulator discovery | HIL setup readiness | `jlink-probe-summary.json`, `jlink-probe-raw.log` |
| LEDs and EN_Peripherals | SW-002, SW-004, SW-012 | Captured GPIO/HIL log |
| External I2C measurement sequence | SW-005, SW-006, SW-007, SW-008, SW-009, SW-010 | Captured measurement and device logs |
| Push-button wake | SW-003, SW-014 | Captured wake/sleep transition log |

## Current Disposition

S8 confirms that the local DA14531 Keil target builds with zero errors and that a J-Link emulator is visible over USB. Final HIL qualification remains open until the built image is intentionally flashed and the target-board tests execute against physical peripherals.
