# Software Lead Execution Plan

## Operating Model

The Software Lead advances work in issue-scoped increments and requires each increment to carry requirements, design, code, tests, review evidence, and CI status.

## Arbitration Rules

| Conflict | Decision Rule |
| --- | --- |
| Dev wants to proceed without tests | Test agent blocks merge until deterministic tests or explicit deferred evidence exist. |
| Requirements are ambiguous | Product requirements agent asks the user before irreversible implementation choices. |
| Hardware is unavailable | Architecture and QA agents must mark the evidence as dev-mode, simulated, or deferred. |
| Security concern is high risk | Security agent blocks release until resolved or explicitly accepted by the human. |

## Current Decision

The current dev-mode vertical slice may remain open for inspection, but the Software Lead does not approve entry into full staged implementation/test until blocking artifact review comments are resolved.

## Immediate Lead Actions

| Action | Owner | Exit Criteria |
| --- | --- | --- |
| Resolve requirements quality comments | Product Requirements Agent | User needs, system requirements, and software requirements have measurable behavior and priorities. |
| Repair RTM overclaims | QA Verification Agent | RTM uses only existing test IDs or creates missing tests with evidence links. |
| Add architecture interface contracts | Systems Architecture Agent | Firmware, BLE, I2C, driver, and PC harness interfaces are named and versioned. |
| Convert stage plan into GitHub issues/PRs | Software Lead Agent | Every stage has branch, PR, test gate, and approval gate. |
| Re-run three-agent review cycle | Software Lead Agent | No blocking comments remain for staged implementation entry. |
