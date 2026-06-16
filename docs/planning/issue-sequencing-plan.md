# Issue Sequencing Plan

## Sequencing Rule

Issues are not executed strictly by requirement number. The Software Lead groups them by dependency and verification gate.

| Sequence | Issue | Requirement | Stage | Dependency | Exit Gate |
| --- | --- | --- | --- | --- | --- |
| 1 | #99 | SW-001 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 2 | #100 | SW-002 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 3 | #101 | SW-003 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 4 | #102 | SW-004 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 5 | #103 | SW-005 | S1 foundation contracts | review-cycle blockers resolved | contract tests and CLI trace tests pass |
| 6 | #104 | SW-006 | S3 sensor and driver adapters | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 7 | #105 | SW-007 | S3 sensor and driver adapters | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 8 | #106 | SW-008 | S3 sensor and driver adapters | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 9 | #107 | SW-009 | S3 sensor and driver adapters | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 10 | #108 | SW-010 | S3 sensor and driver adapters | S1 contracts, S2 BLE/command harness | mock driver tests and integration tests pass |
| 11 | #109 | SW-011 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |
| 12 | #110 | SW-012 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |
| 13 | #111 | SW-013 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |
| 14 | #112 | SW-014 | S1/S6 dev-board constraints and acceptance | S1 contracts and validation decisions | explicit deferred evidence accepted or HIL test passes |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
