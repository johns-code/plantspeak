from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class I2CErrorCode(str, Enum):
    NACK = "nack"
    TIMEOUT = "timeout"
    MISSING_DEVICE = "missing-device"
    INVALID_DATA = "invalid-data"


class I2CDeviceError(RuntimeError):
    def __init__(self, code: I2CErrorCode, address: int, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.address = address


@dataclass(frozen=True)
class I2CTransaction:
    address: int
    write: bytes = b""
    read_length: int = 0
    timeout_ms: int = 100


class MockI2CBus:
    def __init__(self, responses: dict[tuple[int, bytes, int], bytes] | None = None, faults: dict[int, I2CErrorCode] | None = None) -> None:
        self.responses = responses or {}
        self.faults = faults or {}
        self.transactions: list[I2CTransaction] = []

    def transfer(self, transaction: I2CTransaction) -> bytes:
        self.transactions.append(transaction)
        if transaction.address in self.faults:
            code = self.faults[transaction.address]
            raise I2CDeviceError(code, transaction.address, f"I2C {code.value} at 0x{transaction.address:02x}")
        key = (transaction.address, transaction.write, transaction.read_length)
        if key not in self.responses:
            raise I2CDeviceError(I2CErrorCode.MISSING_DEVICE, transaction.address, f"no mock response for 0x{transaction.address:02x}")
        response = self.responses[key]
        if len(response) != transaction.read_length:
            raise I2CDeviceError(I2CErrorCode.INVALID_DATA, transaction.address, "mock response length did not match read length")
        return response
