# User Needs Document

Project: PlantSpeak

| ID | User Need | Success Condition | Scope |
| --- | --- | --- | --- |
| UN-001 | A developer can inspect PlantSpeak ICD capabilities for the DA14531-based device. | CLI reports all supported ICD capabilities and their maturity state. | Dev-mode now, target firmware later |
| UN-002 | A developer can verify DA14531 pin assignments for LEDs, push button, peripheral enable, and I2C. | Pin map reports P0_5, P0_11, P0_10, P0_6, P0_8, and P0_9 with requirement links. | Dev-mode and target |
| UN-003 | A developer can exercise the measurement model without unavailable target-board I2C devices. | `measure --dev-mode` returns deterministic light, temperature, humidity, and acceleration values. | Dev-mode |
| UN-004 | The system preserves target-board hardware intent while making dev-board limitations explicit. | Trace and capability output mark unavailable hardware as substituted, simulated, or deferred. | Dev-mode and target |
| UN-005 | A reviewer can decide what remains before final release. | V-model docs show verification status, validation status, open risks, and deferred evidence. | Release governance |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
