from __future__ import annotations

from dataclasses import dataclass

from plantspeak.adapters.i2c import I2CTransaction, MockI2CBus


ADS1115_ADDRESS = 0x48
HDC2010_ADDRESS = 0x40
MXC4005_ADDRESS = 0x15
MLX90632_ADDRESS = 0x3A
PCA9846_ADDRESS = 0x70
LP5816_ADDRESS = 0x2D


@dataclass(frozen=True)
class AdapterReading:
    name: str
    value: object
    source: str = "mock-i2c"


class ADS1115Driver:
    def __init__(self, bus: MockI2CBus, address: int = ADS1115_ADDRESS) -> None:
        self.bus = bus
        self.address = address

    def read_channel_raw(self, channel: int) -> int:
        data = self.bus.transfer(I2CTransaction(self.address, write=bytes([channel]), read_length=2))
        return int.from_bytes(data, byteorder="big", signed=True)


class HDC2010Driver:
    def __init__(self, bus: MockI2CBus, address: int = HDC2010_ADDRESS) -> None:
        self.bus = bus
        self.address = address

    def read_temperature_humidity(self) -> tuple[float, float]:
        data = self.bus.transfer(I2CTransaction(self.address, write=b"\x00", read_length=4))
        temperature_raw = int.from_bytes(data[:2], byteorder="little")
        humidity_raw = int.from_bytes(data[2:], byteorder="little")
        return (temperature_raw / 100.0, humidity_raw / 100.0)


class MXC4005Driver:
    def __init__(self, bus: MockI2CBus, address: int = MXC4005_ADDRESS) -> None:
        self.bus = bus
        self.address = address

    def read_acceleration(self) -> tuple[float, float, float]:
        data = self.bus.transfer(I2CTransaction(self.address, write=b"\x03", read_length=6))
        axes = [int.from_bytes(data[index : index + 2], byteorder="big", signed=True) / 1000.0 for index in range(0, 6, 2)]
        return (axes[0], axes[1], axes[2])


class MLX90632Driver:
    def __init__(self, bus: MockI2CBus, address: int = MLX90632_ADDRESS) -> None:
        self.bus = bus
        self.address = address

    def read_leaf_temperature(self) -> float:
        data = self.bus.transfer(I2CTransaction(self.address, write=b"\x24", read_length=2))
        return int.from_bytes(data, byteorder="big", signed=True) / 100.0


class PCA9846Driver:
    def __init__(self, bus: MockI2CBus, address: int = PCA9846_ADDRESS) -> None:
        self.bus = bus
        self.address = address

    def select_channel(self, channel: int) -> None:
        if channel < 0 or channel > 3:
            raise ValueError("PCA9846 channel must be 0..3")
        self.bus.transfer(I2CTransaction(self.address, write=bytes([1 << channel]), read_length=0))


class LP5816Driver:
    def __init__(self, bus: MockI2CBus, address: int = LP5816_ADDRESS) -> None:
        self.bus = bus
        self.address = address

    def set_led_current(self, led_index: int, current_ma: int) -> None:
        if led_index < 1 or led_index > 12:
            raise ValueError("LP5816 led_index must be 1..12")
        if current_ma < 0 or current_ma > 25:
            raise ValueError("LP5816 current_ma must be 0..25")
        self.bus.transfer(I2CTransaction(self.address, write=bytes([led_index, current_ma]), read_length=0))
