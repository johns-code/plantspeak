# PlantSpeak Firmware Contract

This directory defines the firmware build and board-probe contract for the DA14531 target.

CI can always validate the reproducible contract layer:

- ICD command IDs in `icd_command_table.h`
- DA14531 pin assignments in `pin_config.h`
- A documented build entry point in `build.ps1`
- A documented non-invasive J-Link probe entry point in `probe-jlink.ps1`
- An operator-gated SmartSnippets flash entry point in `flash-smart-snippets.ps1`
- A live BLE ICD smoke entry point in `run-live-icd-smoke.ps1`

## Build Evidence Policy

When the DA14531 Keil project and uVision toolchain are available, `firmware/build.ps1` is the authoritative build command. Without those local paths, CI validates the firmware contract headers against the Python command and pin contracts.

## Local Keil Build

```powershell
powershell -ExecutionPolicy Bypass -File firmware\build.ps1 `
  -RequireToolchain `
  -UV4Path "C:\Users\johns\AppData\Local\Keil_v5\UV4\UV4.exe" `
  -ProjectPath "C:\Users\johns\531 Project\P531_Handheld\Keil\P531_handheld_firmware.uvprojx" `
  -Target DA14531
```

The script records raw and summarized build evidence under `docs/test-evidence`.

## Local J-Link Probe

```powershell
powershell -ExecutionPolicy Bypass -File firmware\probe-jlink.ps1 -RequireProbe
```

The probe lists connected emulators only. It does not flash, halt, erase, or program the target.

## Local SmartSnippets Flash

```powershell
powershell -ExecutionPolicy Bypass -File firmware\flash-smart-snippets.ps1 -ConfirmFlash
```

The script refuses to erase/write target SPI flash unless `-ConfirmFlash` is supplied.

## Live ICD Smoke

```powershell
powershell -ExecutionPolicy Bypass -File firmware\run-live-icd-smoke.ps1 -RequireLiveBoard
```

The smoke runner invokes the existing P531 `pc_tools\test_icd_regression.py` flow and records raw plus summarized evidence under `docs/test-evidence`.
