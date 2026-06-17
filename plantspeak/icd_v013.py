from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import IntEnum


DOCUMENT_VERSION = "0.13"
PROTOCOL_VERSION = 0x01

PRIMARY_SERVICE_UUID = "9E0F0001-5310-4C1F-AAAA-BBBBCCCCDD01"
RX_CONTROL_UUID = "9E0F0002-5310-4C1F-AAAA-BBBBCCCCDD01"
TX_NOTIFY_UUID = "9E0F0003-5310-4C1F-AAAA-BBBBCCCCDD01"

DEFAULT_ATT_MTU = 23
NEGOTIATED_ATT_MTU_MAX = 67
HEADER_BYTES = 6
CRC_BYTES = 2
MAX_ICD_REQUEST_PAYLOAD = 56
TX_NOTIFICATION_FRAGMENT_BYTES = 20
ATT23_IMAGE_DATA_BYTES = 12
ATT67_IMAGE_DATA_BYTES = 53
RESPONSE_FLAG = 1 << 2
IMAGE_DATA_PAYLOAD_OVERHEAD_BYTES = 3


class ReturnCode(IntEnum):
    OK = 0x00
    UNKNOWN_OPCODE = 0x01
    BAD_PARAM = 0x02
    BUSY = 0x03
    NOT_READY = 0x04
    DENIED = 0x05
    CRC_FAIL = 0x06
    TIMEOUT = 0x07
    TOO_LONG = 0x08
    UNSUPPORTED = 0x09
    LOW_POWER_GUARD = 0x0A


class Opcode(IntEnum):
    PING = 0x01
    GET_INFO = 0x02
    GET_STATUS = 0x03
    SET_TIME = 0x04
    SET_RED_LED = 0x05
    SET_GREEN_LED = 0x06
    SET_PERIPH_POWER = 0x07
    REBOOT = 0x08
    ENTER_DEEP_SLEEP = 0x09
    DEVICE_INFO_SET = 0x0A
    START_MEAS = 0x10
    LOG_GET = 0x14
    LOG_CLEAR = 0x15
    CAL_GET = 0x22
    CAL_SET = 0x23
    IMAGE_BEGIN = 0x40
    IMAGE_DATA = 0x41
    IMAGE_END = 0x42
    LED_CUR_SET = 0x51
    LED_CUR_GET = 0x52


@dataclass(frozen=True)
class CommandSpec:
    opcode: Opcode
    name: str
    request: str
    response: str
    notes: str

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["opcode"] = int(self.opcode)
        return data


COMMAND_SPECS: tuple[CommandSpec, ...] = (
    CommandSpec(Opcode.PING, "PING", "-", "RET, UPTIME_MS:u32", "Liveness check."),
    CommandSpec(Opcode.GET_INFO, "GET_INFO", "-", "RET, FW_VER[3], HW_REV:u8, SERIAL:u32, BUILD_ID:u32", "Identity readback."),
    CommandSpec(Opcode.GET_STATUS, "GET_STATUS", "-", "RET, status struct", "See GET_STATUS_FIELDS."),
    CommandSpec(Opcode.SET_TIME, "SET_TIME", "EPOCH_S:u32", "RET", "Sets handheld time base."),
    CommandSpec(Opcode.SET_RED_LED, "SET_RED_LED", "MODE:u8, PERIOD_100MS:u16, DUTY_PCT:u8", "RET", "MODE 0 off, 1 on, 2 blink."),
    CommandSpec(Opcode.SET_GREEN_LED, "SET_GREEN_LED", "MODE:u8, PERIOD_100MS:u16, DUTY_PCT:u8", "RET", "MODE 0 off, 1 on, 2 blink."),
    CommandSpec(Opcode.SET_PERIPH_POWER, "SET_PERIPH_POWER", "EN:u8", "RET", "Must be ON before START_MEAS."),
    CommandSpec(Opcode.REBOOT, "REBOOT", "-", "RET then disconnect/reset", "Commits pending verified image before reset."),
    CommandSpec(Opcode.ENTER_DEEP_SLEEP, "ENTER_DEEP_SLEEP", "-", "RET then sleep", "Target-board wake validation deferred."),
    CommandSpec(Opcode.DEVICE_INFO_SET, "DEVICE_INFO_SET", "HW_REV:u8, SERIAL:u32", "RET", "Rejects SERIAL=0xFFFFFFFF."),
    CommandSpec(Opcode.START_MEAS, "START_MEAS", "MODE:u8, COUNT:u16, INTERVAL_MS:u16, MEAS_AVG:u8, FLAGS:u8", "RET, measurement frame", "Only MODE=0 implemented."),
    CommandSpec(Opcode.LOG_GET, "LOG_GET", "START_IDX:u16, MAX_ITEMS:u16", "RET, N:u16, N records", "Returns up to 5 records."),
    CommandSpec(Opcode.LOG_CLEAR, "LOG_CLEAR", "-", "RET", "Erases diagnostic log sector."),
    CommandSpec(Opcode.CAL_GET, "CAL_GET", "W_IDX:u8", "RET, CAL_VER, CAL_FLAGS, N, CAL_REC", "W_IDX 0..5 LEDs, W_IDX 6 PPFD."),
    CommandSpec(Opcode.CAL_SET, "CAL_SET", "CAL_REC (11 bytes)", "RET", "NVM commit."),
    CommandSpec(Opcode.IMAGE_BEGIN, "IMAGE_BEGIN", "TYPE:u8, SIZE:u32, VER[3], CRC32:u32", "RET, WINDOW:u16, SLOT:u8", "Starts staged image upload."),
    CommandSpec(Opcode.IMAGE_DATA, "IMAGE_DATA", "OFFSET:u16, BYTES:u8, DATA[BYTES]", "RET", "Use <=12 data bytes at ATT_MTU 23; <=53 at ATT_MTU 67."),
    CommandSpec(Opcode.IMAGE_END, "IMAGE_END", "-", "RET, VERIFY:u8", "VERIFY 0 OK, 1 size mismatch, 2 CRC mismatch, 3 other."),
    CommandSpec(Opcode.LED_CUR_SET, "LED_CUR_SET", "W_IDX:u8, I_LED_UA:u16", "RET", "Only W_IDX 0..5; W_IDX 6 rejected."),
    CommandSpec(Opcode.LED_CUR_GET, "LED_CUR_GET", "W_IDX:u8", "RET, W_IDX:u8, I_LED_UA:u16", "Reads stored physical LED current."),
)

COMMANDS_BY_NAME = {spec.name: spec for spec in COMMAND_SPECS}
COMMANDS_BY_OPCODE = {int(spec.opcode): spec for spec in COMMAND_SPECS}

GET_STATUS_FIELDS = (
    ("UPTIME_MS", "u32", "ms"),
    ("BATT_MV", "u16", "mV"),
    ("PERIPH_PWR", "u8", "bool"),
    ("SENSOR_FLAGS", "u16", "bitmap"),
    ("FAULT_FLAGS", "u16", "bitmap"),
    ("RSSI_DBM", "i8", "dBm"),
    ("LAST_RESET", "u8", "enum"),
    ("HANDHELD_TIME_S", "u32", "s"),
)

START_MEAS_ALLOWED_AVG = (0, 1, 2, 4, 8, 16)

MEASUREMENT_FIELDS = (
    ("RET", "u8"),
    ("MEAS_ID", "u16"),
    ("HANDHELD_TIME_S", "u32"),
    ("SENSORS", "u16"),
    ("TEMP_CC", "i16"),
    ("RH_CPERCENT", "u16"),
    ("PPFD_RAW_MV", "u16"),
    ("LEAF_TEMP_CC", "i16"),
    ("ACCEL_X/Y/Z_MG", "3 x i16"),
    ("ADC_V_MV[12]", "12 x u16"),
    ("BATT_MV", "u16"),
    ("ERRORS", "u16"),
)

WAVELENGTH_CHANNELS = {
    0: "531 nm LED",
    1: "570 nm LED",
    2: "705 nm LED",
    3: "750 nm LED",
    4: "830 nm LED",
    5: "970 nm LED",
    6: "PPFD photodiode pseudo-index",
}

RECOVERY_COMMANDS = (
    Opcode.PING,
    Opcode.GET_INFO,
    Opcode.REBOOT,
    Opcode.IMAGE_BEGIN,
    Opcode.IMAGE_DATA,
    Opcode.IMAGE_END,
)


@dataclass(frozen=True)
class WireFrame:
    opcode: Opcode
    flags: int
    sequence: int
    payload: bytes

    def encode(self) -> bytes:
        if len(self.payload) > MAX_ICD_REQUEST_PAYLOAD:
            raise ValueError("payload exceeds ICD v0.13 maximum request payload")
        header = bytes(
            [
                PROTOCOL_VERSION,
                int(self.opcode),
                self.flags & 0xFF,
                self.sequence & 0xFF,
                len(self.payload) & 0xFF,
                (len(self.payload) >> 8) & 0xFF,
            ]
        )
        frame_without_crc = header + self.payload
        return frame_without_crc + crc16_x25(frame_without_crc).to_bytes(2, "little")

    @staticmethod
    def decode(raw: bytes) -> "WireFrame":
        if len(raw) < HEADER_BYTES + CRC_BYTES:
            raise ValueError("frame is shorter than ICD header plus CRC")
        version = raw[0]
        if version != PROTOCOL_VERSION:
            raise ValueError(f"unsupported ICD protocol version 0x{version:02X}")
        length = raw[4] | (raw[5] << 8)
        expected = HEADER_BYTES + length + CRC_BYTES
        if len(raw) != expected:
            raise ValueError(f"frame length mismatch: expected {expected}, got {len(raw)}")
        expected_crc = int.from_bytes(raw[-2:], "little")
        actual_crc = crc16_x25(raw[:-2])
        if actual_crc != expected_crc:
            raise ValueError("frame CRC mismatch")
        try:
            opcode = Opcode(raw[1])
        except ValueError as exc:
            raise ValueError(f"unknown ICD opcode 0x{raw[1]:02X}") from exc
        return WireFrame(opcode=opcode, flags=raw[2], sequence=raw[3], payload=raw[6:-2])


def crc16_x25(data: bytes) -> int:
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0x8408
            else:
                crc >>= 1
    return (~crc) & 0xFFFF


def gatt_write_value_bytes(att_mtu: int) -> int:
    if att_mtu < DEFAULT_ATT_MTU:
        raise ValueError("ATT_MTU must be at least the default/fallback value")
    return att_mtu - 3


def icd_payload_bytes_for_mtu(att_mtu: int) -> int:
    return max(0, gatt_write_value_bytes(att_mtu) - HEADER_BYTES - CRC_BYTES)


def image_data_bytes_for_single_write(att_mtu: int) -> int:
    return max(0, icd_payload_bytes_for_mtu(att_mtu) - IMAGE_DATA_PAYLOAD_OVERHEAD_BYTES)


def icd_v013_summary() -> dict[str, object]:
    return {
        "document_version": DOCUMENT_VERSION,
        "protocol_version": PROTOCOL_VERSION,
        "uuids": {
            "primary_service": PRIMARY_SERVICE_UUID,
            "rx_control": RX_CONTROL_UUID,
            "tx_notify": TX_NOTIFY_UUID,
        },
        "transport": {
            "default_att_mtu": DEFAULT_ATT_MTU,
            "negotiated_att_mtu_max": NEGOTIATED_ATT_MTU_MAX,
            "max_request_payload": MAX_ICD_REQUEST_PAYLOAD,
            "tx_notification_fragment_bytes": TX_NOTIFICATION_FRAGMENT_BYTES,
            "att23_image_data_bytes": ATT23_IMAGE_DATA_BYTES,
            "att67_image_data_bytes": ATT67_IMAGE_DATA_BYTES,
            "att67_gatt_write_value_bytes": gatt_write_value_bytes(NEGOTIATED_ATT_MTU_MAX),
            "att67_single_write_icd_payload_bytes": icd_payload_bytes_for_mtu(NEGOTIATED_ATT_MTU_MAX),
            "att67_single_write_image_data_bytes": image_data_bytes_for_single_write(NEGOTIATED_ATT_MTU_MAX),
        },
        "commands": [spec.to_dict() for spec in COMMAND_SPECS],
        "return_codes": {code.name: int(code) for code in ReturnCode},
        "start_meas_allowed_avg": list(START_MEAS_ALLOWED_AVG),
        "wavelength_channels": WAVELENGTH_CHANNELS,
        "recovery_commands": [command.name for command in RECOVERY_COMMANDS],
    }
