# Test Report

## Local Test Gate

Status: PASS

Command:

```text
python -m pytest
```

Output:

```text
============================= test session starts =============================
platform win32 -- Python 3.13.9, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\Users\johns\OneDrive\Documents\Software Team\runs\plantspeak-detailed-fresh\delivery-checkout
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.12.1, langsmith-0.7.30
collected 44 items

tests\hil\test_target_board.py sss                                       [  6%]
tests\test_adapters.py .......                                           [ 22%]
tests\test_cli.py ....                                                   [ 31%]
tests\test_contracts.py ..                                               [ 36%]
tests\test_devices.py ....                                               [ 45%]
tests\test_firmware_contracts.py ...                                     [ 52%]
tests\test_hil_gate.py ..                                                [ 56%]
tests\test_icd.py ..                                                     [ 61%]
tests\test_release_evidence.py ..                                        [ 65%]
tests\test_requirements.py .                                             [ 68%]
tests\test_security_transport.py ..                                      [ 72%]
tests\test_system_evidence.py ..                                         [ 77%]
tests\test_traceability.py ..                                            [ 81%]
tests\test_transport.py ........                                         [100%]

======================== 41 passed, 3 skipped in 0.14s ========================
```

## Requirement Coverage

- Software requirements loaded: 14
- Open delivery issues linked: 14
- Covered behavior: requirement registry, pin map, dev-board fallbacks, ICD capability summary, CLI self-test, contract validation, and mechanical traceability.
- S1 evidence: `docs/test-evidence/S1-pytest.txt`, `docs/test-evidence/S1-trace-matrix.json`
- S2 evidence: `docs/test-evidence/S2-pytest.txt`, `docs/test-evidence/s2-devmode/manifest.json`, `docs/test-evidence/s2-devmode/ST-001.json`, `docs/test-evidence/s2-devmode/ST-002.txt`, `docs/test-evidence/s2-devmode/ST-003.json`, `docs/test-evidence/s2-devmode/ST-004.json`
- S3 evidence: `docs/test-evidence/S3-pytest.txt`
- S3 covered behavior: mocked I2C bus success, explicit NACK/timeout/missing-device/invalid-data faults, mux channel validation, LED current validation, and target measurement service snapshot assembly.
- S4 evidence: `docs/test-evidence/S4-pytest.txt`
- S4 covered behavior: ICD frame encode/decode, describe-ICD dispatch, deferred known commands, malformed payload rejection, oversized payload rejection, unsupported command rejection, timeout handling, and no-dispatch behavior for malformed frames.
- S5 evidence: `docs/test-evidence/S5-pytest.txt`
- S5 covered behavior: firmware command table matches Python ICD commands, firmware pin config matches Python pin map, and firmware build script documents contract-only mode plus DA14531 SDK handoff.
- S6 evidence: `docs/test-evidence/S6-pytest.txt`, `docs/test-evidence/ST-006-hil-report.md`, `docs/test-evidence/hil-operator-notes.md`
- S6 covered behavior: HIL gate is disabled by default, can be explicitly enabled by `PLANTSPEAK_TARGET_BOARD=1` or `pytest --target-board`, and target-board tests are skipped in ordinary CI until hardware is present.
- S7 evidence: `docs/test-evidence/S7-pytest.txt`, `docs/release-evidence/release-candidate-manifest.json`
- S7 covered behavior: release manifest references existing required artifacts and explicitly keeps target-board validation deferred pending human/hardware evidence.
