import json

import pytest

from plantspeak.cli import main


def test_capabilities_command_outputs_json(capsys) -> None:
    assert main(["capabilities"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["SW-001"]["command"] == "describe-icd"


def test_icd_v013_command_outputs_wire_contract_json(capsys) -> None:
    assert main(["icd-v013"]) == 0
    output = json.loads(capsys.readouterr().out)

    assert output["document_version"] == "0.13"
    assert output["commands"][0]["name"] == "PING"
    assert output["transport"]["max_request_payload"] == 56


def test_measure_requires_dev_mode() -> None:
    with pytest.raises(SystemExit):
        main(["measure"])


def test_measure_dev_mode_outputs_canned_snapshot(capsys) -> None:
    assert main(["measure", "--dev-mode"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["source"] == "canned-dev-mode-data"


def test_self_test_passes_in_dev_mode(capsys) -> None:
    assert main(["self-test", "--dev-mode"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert all(output.values())
