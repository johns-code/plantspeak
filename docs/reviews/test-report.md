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
collected 11 items

tests\test_cli.py ....                                                   [ 36%]
tests\test_devices.py ....                                               [ 72%]
tests\test_icd.py ..                                                     [ 90%]
tests\test_requirements.py .                                             [100%]

============================= 11 passed in 0.19s ==============================
```

## Requirement Coverage

- Software requirements loaded: 14
- Open delivery issues linked: 14
- Covered behavior: requirement registry, pin map, dev-board fallbacks, ICD capability summary, CLI self-test.
