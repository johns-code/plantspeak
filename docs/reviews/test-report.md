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
collected 17 items

tests\test_cli.py ....                                                   [ 23%]
tests\test_contracts.py ..                                               [ 35%]
tests\test_devices.py ....                                               [ 58%]
tests\test_icd.py ..                                                     [ 70%]
tests\test_requirements.py .                                             [ 76%]
tests\test_system_evidence.py ..                                         [ 88%]
tests\test_traceability.py ..                                            [100%]

============================= 17 passed in 0.14s ==============================
```

## Requirement Coverage

- Software requirements loaded: 14
- Open delivery issues linked: 14
- Covered behavior: requirement registry, pin map, dev-board fallbacks, ICD capability summary, CLI self-test, contract validation, and mechanical traceability.
- S1 evidence: `docs/test-evidence/S1-pytest.txt`, `docs/test-evidence/S1-trace-matrix.json`
- S2 evidence: `docs/test-evidence/S2-pytest.txt`, `docs/test-evidence/s2-devmode/manifest.json`, `docs/test-evidence/s2-devmode/ST-001.json`, `docs/test-evidence/s2-devmode/ST-002.txt`, `docs/test-evidence/s2-devmode/ST-003.json`, `docs/test-evidence/s2-devmode/ST-004.json`
