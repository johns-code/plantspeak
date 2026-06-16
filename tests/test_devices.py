from plantspeak.devices import build_capability_map, collect_dev_mode_snapshot, default_dev_board_profile
from plantspeak.pins import pin_map


def test_dev_board_profile_tracks_unavailable_hardware() -> None:
    profile = default_dev_board_profile()
    assert not profile.has_external_i2c
    assert not profile.has_user_button
    assert profile.transport == "ble"


def test_pin_assignments_match_requirements() -> None:
    pins = pin_map()
    assert pins["red_user_led"].pin == "P0_5"
    assert pins["green_user_led"].pin == "P0_11"
    assert pins["user_push_button"].pin == "P0_10"
    assert pins["en_peripherals"].pin == "P0_6"
    assert pins["i2c_scl"].pin == "P0_8"
    assert pins["i2c_sda"].pin == "P0_9"


def test_canned_sensor_snapshot_supports_dev_mode() -> None:
    snapshot = collect_dev_mode_snapshot()
    assert snapshot.source == "canned-dev-mode-data"
    assert snapshot.ppfd_umol_m2_s > 0
    assert snapshot.to_dict()["acceleration_g"] == [0.01, -0.02, 1.0]


def test_capability_map_marks_deferred_hardware() -> None:
    capabilities = build_capability_map()
    assert capabilities["SW-006"] == "canned-data"
    assert capabilities["SW-013"] == "canned-data"
    assert capabilities["SW-014"] == "dev-board-unavailable"
