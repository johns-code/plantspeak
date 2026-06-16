# HIL Operator Notes

The HIL suite is intentionally gated behind `PLANTSPEAK_TARGET_BOARD=1` so CI cannot accidentally claim target-board verification.

## Before Running

1. Flash the DA14531 firmware image produced by the S5/S6 build path.
2. Connect the target board and external peripherals.
3. Confirm the PC transport path is available.
4. Set `PLANTSPEAK_TARGET_BOARD=1`.
5. Run `python -m pytest tests/hil --target-board`.

## Failure Rule

Any HIL failure must create or update the GitHub issue for the affected requirement and attach the captured board log.
