# Risk Register

| Risk | Impact | Mitigation | Status |
| --- | --- | --- | --- |
| Target-board hardware is unavailable | Cannot complete hardware-in-loop verification. | Mark dev-mode evidence clearly and defer target-board tests. | Open |
| BLE transport not implemented | PC-to-device ICD execution cannot be proven yet. | Keep CLI and ICD model stable; add BLE adapter next. | Open |
| Canned data hides sensor integration defects | Real I2C sequencing may differ. | Preserve adapter boundary and add integration tests when hardware arrives. | Open |
| User push button unavailable | Wake-from-sleep validation cannot run on dev board. | Track as explicit deferred acceptance item. | Open |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
