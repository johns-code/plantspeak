from tests.hil.test_target_board import target_board_enabled


def test_hil_gate_is_disabled_by_default(monkeypatch) -> None:
    monkeypatch.delenv("PLANTSPEAK_TARGET_BOARD", raising=False)

    assert target_board_enabled() is False


def test_hil_gate_can_be_enabled_explicitly(monkeypatch) -> None:
    monkeypatch.setenv("PLANTSPEAK_TARGET_BOARD", "1")

    assert target_board_enabled() is True
