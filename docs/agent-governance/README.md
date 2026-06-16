# Agent Governance Report

## Software Lead

The `software_lead` agent orchestrates lifecycle flow, arbitrates disputes, and protects quality policy before human approval.

## Roles

| Role ID | Title | Lenses |
| --- | --- | --- |
| software_lead | Software Lead Agent | systems thinking, delivery risk, quality policy, tradeoff arbitration |
| product_requirements | Product Requirements Agent | user value, requirement clarity, acceptance validity |
| systems_architecture | Systems Architecture Agent | architecture risk, modularity, traceability |
| test_verification | Test and Verification Agent | testability, coverage, evidence quality |
| security_review | Security Review Agent | threat modeling, dependency risk, secret exposure |
| release_quality | Release Quality Agent | release readiness, auditability, human approval |

## Artifact Reviews

| Artifact | Reviewer | Lens | Verdict |
| --- | --- | --- | --- |
| Architecture/Design Document | product_requirements | user value | approved_with_conditions |
| Architecture/Design Document | systems_architecture | architecture risk | approved_with_conditions |
| Architecture/Design Document | security_review | threat modeling | approved_with_conditions |
| Detailed Design Notes | systems_architecture | modularity | approved_with_conditions |
| Detailed Design Notes | test_verification | testability | approved_with_conditions |
| Detailed Design Notes | release_quality | auditability | approved_with_conditions |
| Test Strategy | product_requirements | acceptance validity | approved_with_conditions |
| Test Strategy | test_verification | coverage | approved_with_conditions |
| Test Strategy | security_review | dependency risk | approved_with_conditions |

## Arbitration

| ID | Topic | Decision |
| --- | --- | --- |
| ARB-001 | Verification standard for Detailed Design Notes | Development may proceed only with requirement-linked tests and recorded evidence. |
| ARB-002 | Verification standard for Test Strategy | Development may proceed only with requirement-linked tests and recorded evidence. |

## Quality Policy

| Policy | Status | Details |
| --- | --- | --- |
| design-artifacts-have-three-reviews | PASS | Each design artifact must have at least three independent role/lens reviews. |
| software-lead-arbitration-recorded | PASS | Software lead arbitration must be recorded for dev/test quality tension. |
| requirements-have-trace-links | PASS | Every software requirement must link to tasks, tests, and verification evidence placeholders. |
