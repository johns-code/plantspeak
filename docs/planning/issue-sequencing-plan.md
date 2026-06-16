# Issue Sequencing Plan

## Sequencing Rule

Issues are not executed strictly by requirement number. The Software Lead groups them by dependency and verification gate.

| Sequence | Issue | Requirement | Stage | Dependency | Exit Gate |
| --- | --- | --- | --- | --- | --- |
| 1 | #114 | SW-001 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 2 | #115 | SW-002 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 3 | #116 | SW-003 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 4 | #117 | SW-004 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 5 | #118 | SW-005 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 6 | #119 | SW-006 | S3 hardware adapter layer | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 7 | #120 | SW-007 | S3 hardware adapter layer | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 8 | #121 | SW-008 | S3 hardware adapter layer | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 9 | #122 | SW-009 | S3 hardware adapter layer | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 10 | #123 | SW-010 | S3 hardware adapter layer | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 11 | #124 | SW-011 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |
| 12 | #125 | SW-012 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |
| 13 | #126 | SW-013 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |
| 14 | #127 | SW-014 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
