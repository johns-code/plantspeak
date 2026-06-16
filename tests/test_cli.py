from plantspeak.cli import main


def test_list_requirements_outputs_records(capsys) -> None:
    assert main(["list-requirements"]) == 0
    output = capsys.readouterr().out
    assert "SW-001" in output


def test_trace_outputs_verification_status(capsys) -> None:
    assert main(["trace"]) == 0
    output = capsys.readouterr().out
    assert "verification pending" in output
