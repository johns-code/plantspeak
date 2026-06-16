# Test Strategy

Project: PlantSpeak

## Strategy

Testing follows the right side of the V-model and separates dev-board evidence from target-board evidence.

| Level | Scope | Gate |
| --- | --- | --- |
| Unit verification | Requirements registry, pin map, ICD command map, device profile, canned snapshot. | `python -m pytest` |
| Integration verification | CLI commands integrating requirements, issue links, ICD map, and device profile. | `python -m pytest tests/test_cli.py` |
| System verification | Dev-mode self-test and trace output prove the current system behavior. | CI run on PR |
| User acceptance validation | Human confirms dev-mode scope and deferred target hardware evidence. | Explicit approval before merge/release |

## Authoritative Gates

Local test output is useful evidence, but GitHub Actions on the PR is the authoritative automated gate.
