# PlantSpeak

PlantSpeak is being developed through the V-model agentic development engine.

This branch contains the first autopilot-driven vertical slice: a Python dev-mode harness that models the requested DA14531 ICD capabilities, hardware pin assignments, unavailable dev-board features, canned sensor readings, traceability data, and deterministic tests.

## Commands

```powershell
python -m plantspeak.cli list-requirements
python -m plantspeak.cli trace
python -m plantspeak.cli capabilities
python -m plantspeak.cli measure --dev-mode
python -m plantspeak.cli self-test --dev-mode
```

## Current Scope

- Implements inspectable ICD capability and hardware-abstraction behavior for software planning and verification.
- Uses canned sensor values because external I2C devices are not present on the dev board.
- Defers DA14531 firmware flashing, BLE transport execution, and hardware-in-loop wake-from-sleep validation to later implementation increments.
