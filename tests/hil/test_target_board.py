import os

import pytest


pytestmark = pytest.mark.hil


def target_board_enabled() -> bool:
    return os.getenv("PLANTSPEAK_TARGET_BOARD") == "1"


@pytest.mark.skipif(not target_board_enabled(), reason="target board HIL requires PLANTSPEAK_TARGET_BOARD=1")
def test_target_board_leds_and_peripheral_enable() -> None:
    raise NotImplementedError("Connect DA14531 HIL fixture and assert P0_5, P0_11, and P0_6 behavior.")


@pytest.mark.skipif(not target_board_enabled(), reason="target board HIL requires PLANTSPEAK_TARGET_BOARD=1")
def test_target_board_i2c_measurement_sequence() -> None:
    raise NotImplementedError("Connect DA14531 HIL fixture and assert external I2C device measurement sequence.")


@pytest.mark.skipif(not target_board_enabled(), reason="target board HIL requires PLANTSPEAK_TARGET_BOARD=1")
def test_target_board_push_button_wake() -> None:
    raise NotImplementedError("Connect DA14531 HIL fixture and assert P0_10 wake-from-sleep behavior.")
