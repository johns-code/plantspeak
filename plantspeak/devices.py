from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class DevBoardProfile:
    name: str
    has_user_leds: bool
    has_user_button: bool
    has_en_peripherals: bool
    has_external_i2c: bool
    transport: str


@dataclass(frozen=True)
class SensorSnapshot:
    photodiode_current_ua: float
    ppfd_umol_m2_s: float
    leaf_temperature_c: float
    ambient_temperature_c: float
    relative_humidity_percent: float
    acceleration_g: tuple[float, float, float]
    source: str

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["acceleration_g"] = list(self.acceleration_g)
        return data


def default_dev_board_profile() -> DevBoardProfile:
    return DevBoardProfile(
        name="DA14531 development board",
        has_user_leds=False,
        has_user_button=False,
        has_en_peripherals=False,
        has_external_i2c=False,
        transport="ble",
    )


def collect_dev_mode_snapshot(profile: DevBoardProfile | None = None) -> SensorSnapshot:
    selected = profile or default_dev_board_profile()
    source = "canned-dev-mode-data" if not selected.has_external_i2c else "i2c"
    return SensorSnapshot(
        photodiode_current_ua=12.5,
        ppfd_umol_m2_s=245.0,
        leaf_temperature_c=24.2,
        ambient_temperature_c=23.6,
        relative_humidity_percent=51.0,
        acceleration_g=(0.01, -0.02, 1.0),
        source=source,
    )


def build_capability_map(profile: DevBoardProfile | None = None) -> dict[str, str]:
    selected = profile or default_dev_board_profile()
    unavailable = "dev-board-unavailable"
    return {
        "SW-001": "modeled",
        "SW-002": "dev-board-led-substitute" if not selected.has_user_leds else "hardware",
        "SW-003": unavailable if not selected.has_user_button else "hardware",
        "SW-004": unavailable if not selected.has_en_peripherals else "hardware",
        "SW-005": unavailable if not selected.has_external_i2c else "hardware",
        "SW-006": "canned-data" if not selected.has_external_i2c else "hardware",
        "SW-007": "canned-data" if not selected.has_external_i2c else "hardware",
        "SW-008": "canned-data" if not selected.has_external_i2c else "hardware",
        "SW-009": "canned-data" if not selected.has_external_i2c else "hardware",
        "SW-010": "canned-data" if not selected.has_external_i2c else "hardware",
        "SW-011": "dev-board-led-substitute",
        "SW-012": unavailable,
        "SW-013": "canned-data",
        "SW-014": unavailable,
    }
