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

Proceed with a dev-mode vertical slice. Defer target-board hardware-in-loop tests until target hardware and firmware transport are available.
