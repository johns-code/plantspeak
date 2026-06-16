from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PinAssignment:
    signal: str
    pin: str
    requirement_id: str
    available_on_dev_board: bool
    notes: str = ""


PIN_ASSIGNMENTS: tuple[PinAssignment, ...] = (
    PinAssignment("red_user_led", "P0_5", "SW-002", False, "Use dev-board LED for early testing."),
    PinAssignment("green_user_led", "P0_11", "SW-002", False, "Use dev-board LED for early testing."),
    PinAssignment("user_push_button", "P0_10", "SW-003", False, "Wake-from-sleep testing needs target hardware."),
    PinAssignment("en_peripherals", "P0_6", "SW-004", False, "Not available on dev board."),
    PinAssignment("i2c_scl", "P0_8", "SW-005", False, "External I2C devices are represented by canned data in dev mode."),
    PinAssignment("i2c_sda", "P0_9", "SW-005", False, "External I2C devices are represented by canned data in dev mode."),
)


def pin_map() -> dict[str, PinAssignment]:
    return {assignment.signal: assignment for assignment in PIN_ASSIGNMENTS}
