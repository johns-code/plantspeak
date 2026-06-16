# PlantSpeak Firmware Contract

This directory defines the S5 firmware build contract for the DA14531 target.

The current repository does not include the DA14531 vendor SDK or a flashable firmware image. S5 therefore provides a reproducible contract layer that CI can validate:

- ICD command IDs in `icd_command_table.h`
- DA14531 pin assignments in `pin_config.h`
- A documented build entry point in `build.ps1`

## Build Evidence Policy

When the DA14531 SDK/toolchain is available, `firmware/build.ps1` must become the authoritative build command. Until then, CI validates the firmware contract headers against the Python command and pin contracts.

## Manual Build Placeholder

```powershell
pwsh firmware/build.ps1 -Configuration Release
```

The script currently exits successfully in contract-only mode and prints the expected SDK handoff point.
