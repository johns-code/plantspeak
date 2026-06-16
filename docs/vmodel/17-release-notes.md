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

## Included

- PC/dev-mode command harness.
- Requirement traceability and issue links.
- Deterministic local tests and PR CI gate.
- Explicit deferred hardware status reporting.

## Gate Status

- Local tests: PASS
- PR CI: required and tracked in GitHub Actions
- Human release approval: pending

## Not Included

- DA14531 firmware image.
- BLE transport implementation.
- Target-board hardware-in-loop evidence.

## Firmware Note

The repository now contains firmware contract artifacts, but not a flashable DA14531 firmware image. `firmware/build.ps1` runs in contract-only mode unless `DA14531_SDK_PATH` is configured and a project-specific SDK build command is added.

## Known Deferred Scope

- Target-board I2C devices, LED sequencing, EN_Peripherals, and push-button wake require later firmware/HIL stages.
- Security approval does not cover BLE or firmware command execution until those stages exist.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
