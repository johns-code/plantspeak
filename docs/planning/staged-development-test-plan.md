# Staged Development And Test Plan

## Readiness Decision

Status: blocked before full staged implementation.

Reason: three-agent artifact review found blocking gaps in requirements, architecture contracts, RTM accuracy, verification evidence, acceptance criteria, and release/security review posture.

## Stages

| Stage | Goal | Branch Pattern | Primary Agents | Required Tests | Exit Criteria |
| --- | --- | --- | --- | --- | --- |
| S0 review remediation | Fix blocking artifact comments before implementation claims advance. | `agent/review-remediation-*` | Software Lead, Product, Architecture, QA | doc quality checks, review-cycle regeneration | No blocking review comments for staged implementation entry. |
| S1 foundation contracts | Define stable command, data, pin, requirement, and trace contracts. | `agent/foundation-contracts-*` | Architecture, Development, QA | unit tests for schemas, pins, capability registry, RTM integrity | Contract tests pass and docs link DES/TASK/TEST IDs to code. |
| S2 PC dev-mode harness | Make PC-side CLI and dev-mode behavior executable and user-inspectable. | `agent/devmode-harness-*` | Development, QA, Product | CLI tests, snapshot tests, self-test JSON checks | PR proves dev-mode measurement, trace, and self-test outputs. |
| S3 hardware adapter layer | Add interfaces for ADS1115, LP5816/PCA9846, MLX90632, HDC2010, MXC4005XC without target hardware dependency. | `agent/hardware-adapters-*` | Architecture, Development, Security | mock I2C tests, mux-channel tests, error-path tests | Adapter contract tests pass and target-board gaps remain explicit. |
| S4 BLE/ICD transport | Add transport abstraction and simulated BLE command execution. | `agent/ble-transport-*` | Development, Security, QA | simulated transport tests, malformed payload tests | PC harness can issue ICD commands through transport abstraction. |
| S5 DA14531 firmware build path | Add firmware project/build/flash workflow when toolchain details are verified. | `agent/firmware-build-*` | Firmware Dev, Release, QA | build command, static checks, flash dry-run where safe | CI or documented local evidence proves reproducible firmware build. |
| S6 hardware-in-loop qualification | Run target-board tests for LEDs, EN_Peripherals, I2C sensors, measurement sequence, and push-button wake. | `agent/hil-qualification-*` | QA, Firmware Dev, Product | HIL tests with captured logs and operator notes | Requirement-by-requirement verification closure or accepted deferral. |
| S7 acceptance and release | Close validation, security, code review, release notes, and human approval gates. | `agent/release-candidate-*` | Software Lead, Release, Security, Product | full CI, review checklist, security scan, acceptance checklist | Human signs final acceptance and release package is generated. |

## PR Rules

- Each stage opens one or more issue-linked PRs.
- Every PR must update V-model docs, tests, traceability, and review evidence.
- CI is authoritative for automated gates.
- The Software Lead cannot waive failing deterministic gates; only the human can accept documented deferred evidence.

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
