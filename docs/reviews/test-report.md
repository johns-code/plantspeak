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
collected 24 items

tests\test_adapters.py .......                                           [ 29%]
tests\test_cli.py ....                                                   [ 45%]
tests\test_contracts.py ..                                               [ 54%]
tests\test_devices.py ....                                               [ 70%]
tests\test_icd.py ..                                                     [ 79%]
tests\test_requirements.py .                                             [ 83%]
tests\test_system_evidence.py ..                                         [ 91%]
tests\test_traceability.py ..                                            [100%]

============================= 24 passed in 0.12s ==============================
```

## Requirement Coverage

- Software requirements loaded: 14
- Open delivery issues linked: 14
- Covered behavior: requirement registry, pin map, dev-board fallbacks, ICD capability summary, CLI self-test, contract validation, and mechanical traceability.
- S1 evidence: `docs/test-evidence/S1-pytest.txt`, `docs/test-evidence/S1-trace-matrix.json`
- S2 evidence: `docs/test-evidence/S2-pytest.txt`, `docs/test-evidence/s2-devmode/manifest.json`, `docs/test-evidence/s2-devmode/ST-001.json`, `docs/test-evidence/s2-devmode/ST-002.txt`, `docs/test-evidence/s2-devmode/ST-003.json`, `docs/test-evidence/s2-devmode/ST-004.json`
- S3 evidence: `docs/test-evidence/S3-pytest.txt`
- S3 covered behavior: mocked I2C bus success, explicit NACK/timeout/missing-device/invalid-data faults, mux channel validation, LED current validation, and target measurement service snapshot assembly.
