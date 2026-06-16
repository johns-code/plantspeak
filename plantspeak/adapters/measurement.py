from __future__ import annotations

from dataclasses import dataclass

from plantspeak.adapters.devices import ADS1115Driver, HDC2010Driver, MLX90632Driver, MXC4005Driver
from plantspeak.devices import SensorSnapshot


@dataclass(frozen=True)
class TargetMeasurementService:
    ads1115: ADS1115Driver
    hdc2010: HDC2010Driver
    mlx90632: MLX90632Driver
    mxc4005: MXC4005Driver

    def collect_snapshot(self) -> SensorSnapshot:
        photodiode_raw = self.ads1115.read_channel_raw(0)
        ppfd_raw = self.ads1115.read_channel_raw(1)
        ambient_temp, humidity = self.hdc2010.read_temperature_humidity()
        leaf_temp = self.mlx90632.read_leaf_temperature()
        acceleration = self.mxc4005.read_acceleration()
        return SensorSnapshot(
            photodiode_current_ua=photodiode_raw / 100.0,
            ppfd_umol_m2_s=float(ppfd_raw),
            leaf_temperature_c=leaf_temp,
            ambient_temperature_c=ambient_temp,
            relative_humidity_percent=humidity,
            acceleration_g=acceleration,
            source="target-i2c",
        )
