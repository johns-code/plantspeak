# Release Notes

Project: PlantSpeak

## Candidate Version

0.2.0 dev-mode vertical slice.

## Added

- PlantSpeak ICD capability model.
- Dev-board hardware profile and pin assignment registry.
- Canned sensor measurement path for external I2C devices unavailable on the dev board.
- CLI commands for requirements, traceability, capability summary, measurement, and self-test.
- Unit, integration, and system-level dev-mode tests.
- V-model planning, traceability, review, security, and test evidence.
- Firmware contract headers and build handoff documentation.
- Real local DA14531 Keil build gate with zero-error evidence.
- Non-invasive J-Link emulator discovery gate.

## Included

- PC/dev-mode command harness.
- Requirement traceability and issue links.
- Deterministic local tests and PR CI gate.
- Explicit deferred hardware status reporting.

## Gate Status

- Local tests: 43 passed, 3 skipped
- PR CI: required and tracked in GitHub Actions
- Human release approval: pending
- Release candidate manifest: `docs/release-evidence/release-candidate-manifest.json`

## Not Included

- DA14531 firmware flash evidence.
- BLE transport implementation.
- Target-board hardware-in-loop evidence.

## Firmware Note

The repository now contains firmware contract artifacts plus repeatable local gates for the known DA14531 Keil project. `firmware/build.ps1` runs in contract-only mode in generic CI unless the local Keil project and uVision paths are supplied.

## Known Deferred Scope

- Target-board I2C devices, LED sequencing, EN_Peripherals, and push-button wake require later firmware/HIL stages.
- Security approval does not cover BLE or firmware command execution until those stages exist.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
