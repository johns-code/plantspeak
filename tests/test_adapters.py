import pytest

from plantspeak.adapters.devices import (
    ADS1115_ADDRESS,
    HDC2010_ADDRESS,
    LP5816_ADDRESS,
    MLX90632_ADDRESS,
    MXC4005_ADDRESS,
    PCA9846_ADDRESS,
    ADS1115Driver,
    HDC2010Driver,
    LP5816Driver,
    MLX90632Driver,
    MXC4005Driver,
    PCA9846Driver,
)
from plantspeak.adapters.i2c import I2CDeviceError, I2CErrorCode, MockI2CBus
from plantspeak.adapters.measurement import TargetMeasurementService


def test_mock_i2c_bus_returns_scripted_response() -> None:
    bus = MockI2CBus({(ADS1115_ADDRESS, b"\x00", 2): b"\x04\xd2"})

    assert ADS1115Driver(bus).read_channel_raw(0) == 1234


@pytest.mark.parametrize("fault", [I2CErrorCode.NACK, I2CErrorCode.TIMEOUT, I2CErrorCode.MISSING_DEVICE])
def test_mock_i2c_bus_reports_explicit_faults(fault: I2CErrorCode) -> None:
    bus = MockI2CBus(faults={ADS1115_ADDRESS: fault})

    with pytest.raises(I2CDeviceError) as excinfo:
        ADS1115Driver(bus).read_channel_raw(0)

    assert excinfo.value.code == fault
    assert excinfo.value.address == ADS1115_ADDRESS


def test_mock_i2c_bus_rejects_invalid_data_length() -> None:
    bus = MockI2CBus({(ADS1115_ADDRESS, b"\x00", 2): b"\x01"})

    with pytest.raises(I2CDeviceError) as excinfo:
        ADS1115Driver(bus).read_channel_raw(0)

    assert excinfo.value.code == I2CErrorCode.INVALID_DATA


def test_mux_and_led_drivers_validate_arguments() -> None:
    bus = MockI2CBus(
        {
            (PCA9846_ADDRESS, b"\x02", 0): b"",
            (LP5816_ADDRESS, b"\x03\x0a", 0): b"",
        }
    )

    PCA9846Driver(bus).select_channel(1)
    LP5816Driver(bus).set_led_current(3, 10)

    with pytest.raises(ValueError):
        PCA9846Driver(bus).select_channel(4)
    with pytest.raises(ValueError):
        LP5816Driver(bus).set_led_current(13, 10)


def test_target_measurement_service_collects_mocked_snapshot() -> None:
    bus = MockI2CBus(
        {
            (ADS1115_ADDRESS, b"\x00", 2): b"\x04\xd2",
            (ADS1115_ADDRESS, b"\x01", 2): b"\x00\xf5",
            (HDC2010_ADDRESS, b"\x00", 4): b"\x38\x09\xec\x13",
            (MLX90632_ADDRESS, b"\x24", 2): b"\x09\x74",
            (MXC4005_ADDRESS, b"\x03", 6): b"\x00\x0a\xff\xec\x03\xe8",
        }
    )

    snapshot = TargetMeasurementService(
        ads1115=ADS1115Driver(bus),
        hdc2010=HDC2010Driver(bus),
        mlx90632=MLX90632Driver(bus),
        mxc4005=MXC4005Driver(bus),
    ).collect_snapshot()

    assert snapshot.photodiode_current_ua == 12.34
    assert snapshot.ppfd_umol_m2_s == 245.0
    assert snapshot.ambient_temperature_c == 23.6
    assert snapshot.relative_humidity_percent == 51.0
    assert snapshot.leaf_temperature_c == 24.2
    assert snapshot.acceleration_g == (0.01, -0.02, 1.0)
    assert snapshot.source == "target-i2c"
