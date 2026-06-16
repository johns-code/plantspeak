# Implementation Task Plan

Project: PlantSpeak

## Task Policy

The Software Lead owns sequencing. Development may proceed when a task has an issue, requirement link, design target, test evidence, and deterministic gate. Test and security agents can block release evidence; the Software Lead arbitrates but cannot waive deterministic gates.

| Task | Issue | Requirement | Primary Code | Status | Exit Gate |
| --- | --- | --- | --- | --- | --- |
| TASK-001 | #99 | SW-001 | plantspeak/icd.py | implemented-dev-mode | pytest, CI, human review |
| TASK-002 | #100 | SW-002 | plantspeak/pins.py, plantspeak/devices.py | implemented-dev-mode | pytest, CI, human review |
| TASK-003 | #101 | SW-003 | plantspeak/pins.py, plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-004 | #102 | SW-004 | plantspeak/pins.py, plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-005 | #103 | SW-005 | plantspeak/pins.py, plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-006 | #104 | SW-006 | plantspeak/devices.py | implemented-dev-mode | pytest, CI, human review |
| TASK-007 | #105 | SW-007 | plantspeak/icd.py, plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-008 | #106 | SW-008 | plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-009 | #107 | SW-009 | plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-010 | #108 | SW-010 | plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-011 | #109 | SW-011 | plantspeak/devices.py | implemented-dev-mode | pytest, CI, human review |
| TASK-012 | #110 | SW-012 | plantspeak/devices.py | modeled-or-deferred | pytest, CI, human review |
| TASK-013 | #111 | SW-013 | plantspeak/devices.py | implemented-dev-mode | pytest, CI, human review |
| TASK-014 | #112 | SW-014 | plantspeak/devices.py, plantspeak/icd.py | modeled-or-deferred | pytest, CI, human review |

## Review Remediation Closure

| Review Theme | Resolution |
| --- | --- |
| Three-agent review comments | Addressed in this artifact by adding concrete scope, evidence, and gate language. |
| Staged implementation readiness | This artifact now distinguishes dev-mode evidence from deferred target-board evidence. |
| Software Lead disposition | Cleared for S0 review-remediation exit, subject to regenerated review cycle and CI. |
