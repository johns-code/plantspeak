import pytest

from plantspeak.icd_v013 import (
    ATT23_IMAGE_DATA_BYTES,
    ATT67_IMAGE_DATA_BYTES,
    COMMANDS_BY_NAME,
    COMMANDS_BY_OPCODE,
    DEFAULT_ATT_MTU,
    DOCUMENT_VERSION,
    MAX_ICD_REQUEST_PAYLOAD,
    NEGOTIATED_ATT_MTU_MAX,
    PRIMARY_SERVICE_UUID,
    RECOVERY_COMMANDS,
    RESPONSE_FLAG,
    RX_CONTROL_UUID,
    START_MEAS_ALLOWED_AVG,
    TX_NOTIFICATION_FRAGMENT_BYTES,
    TX_NOTIFY_UUID,
    WAVELENGTH_CHANNELS,
    WireFrame,
    Opcode,
    ReturnCode,
    crc16_x25,
    icd_v013_summary,
)


def test_icd_v013_metadata_matches_source_document() -> None:
    assert DOCUMENT_VERSION == "0.13"
    assert PRIMARY_SERVICE_UUID == "9E0F0001-5310-4C1F-AAAA-BBBBCCCCDD01"
    assert RX_CONTROL_UUID == "9E0F0002-5310-4C1F-AAAA-BBBBCCCCDD01"
    assert TX_NOTIFY_UUID == "9E0F0003-5310-4C1F-AAAA-BBBBCCCCDD01"
    assert DEFAULT_ATT_MTU == 23
    assert NEGOTIATED_ATT_MTU_MAX == 67
    assert MAX_ICD_REQUEST_PAYLOAD == 56
    assert TX_NOTIFICATION_FRAGMENT_BYTES == 20
    assert ATT23_IMAGE_DATA_BYTES == 12
    assert ATT67_IMAGE_DATA_BYTES == 53


def test_icd_v013_opcode_table_matches_source_document() -> None:
    expected = {
        "PING": 0x01,
        "GET_INFO": 0x02,
        "GET_STATUS": 0x03,
        "SET_TIME": 0x04,
        "SET_RED_LED": 0x05,
        "SET_GREEN_LED": 0x06,
        "SET_PERIPH_POWER": 0x07,
        "REBOOT": 0x08,
        "ENTER_DEEP_SLEEP": 0x09,
        "DEVICE_INFO_SET": 0x0A,
        "START_MEAS": 0x10,
        "LOG_GET": 0x14,
        "LOG_CLEAR": 0x15,
        "CAL_GET": 0x22,
        "CAL_SET": 0x23,
        "IMAGE_BEGIN": 0x40,
        "IMAGE_DATA": 0x41,
        "IMAGE_END": 0x42,
        "LED_CUR_SET": 0x51,
        "LED_CUR_GET": 0x52,
    }

    assert {name: int(spec.opcode) for name, spec in COMMANDS_BY_NAME.items()} == expected
    assert set(COMMANDS_BY_OPCODE) == set(expected.values())


def test_icd_v013_return_codes_match_source_document() -> None:
    assert {code.name: int(code) for code in ReturnCode} == {
        "OK": 0x00,
        "UNKNOWN_OPCODE": 0x01,
        "BAD_PARAM": 0x02,
        "BUSY": 0x03,
        "NOT_READY": 0x04,
        "DENIED": 0x05,
        "CRC_FAIL": 0x06,
        "TIMEOUT": 0x07,
        "TOO_LONG": 0x08,
        "UNSUPPORTED": 0x09,
        "LOW_POWER_GUARD": 0x0A,
    }


def test_icd_v013_measurement_and_calibration_rules() -> None:
    assert START_MEAS_ALLOWED_AVG == (0, 1, 2, 4, 8, 16)
    assert WAVELENGTH_CHANNELS[0] == "531 nm LED"
    assert WAVELENGTH_CHANNELS[5] == "970 nm LED"
    assert WAVELENGTH_CHANNELS[6] == "PPFD photodiode pseudo-index"
    assert "W_IDX 0..5" in COMMANDS_BY_NAME["LED_CUR_SET"].notes
    assert "W_IDX 6 rejected" in COMMANDS_BY_NAME["LED_CUR_SET"].notes


def test_icd_v013_recovery_subset() -> None:
    assert tuple(command.name for command in RECOVERY_COMMANDS) == (
        "PING",
        "GET_INFO",
        "REBOOT",
        "IMAGE_BEGIN",
        "IMAGE_DATA",
        "IMAGE_END",
    )


def test_icd_v013_wire_frame_roundtrip_and_crc() -> None:
    frame = WireFrame(opcode=Opcode.SET_PERIPH_POWER, flags=0, sequence=0x22, payload=b"\x01")
    encoded = frame.encode()

    assert encoded[:6] == bytes([0x01, 0x07, 0x00, 0x22, 0x01, 0x00])
    assert int.from_bytes(encoded[-2:], "little") == crc16_x25(encoded[:-2])
    assert WireFrame.decode(encoded) == frame


def test_icd_v013_response_frame_flag_is_bit_2() -> None:
    response = WireFrame(opcode=Opcode.PING, flags=RESPONSE_FLAG, sequence=1, payload=bytes([ReturnCode.OK, 1, 0, 0, 0]))

    decoded = WireFrame.decode(response.encode())

    assert decoded.flags & RESPONSE_FLAG
    assert decoded.payload[0] == ReturnCode.OK


def test_icd_v013_wire_frame_rejects_bad_crc_and_oversized_payload() -> None:
    encoded = bytearray(WireFrame(opcode=Opcode.PING, flags=0, sequence=1, payload=b"").encode())
    encoded[-1] ^= 0xFF

    with pytest.raises(ValueError, match="CRC"):
        WireFrame.decode(bytes(encoded))

    with pytest.raises(ValueError, match="maximum request payload"):
        WireFrame(opcode=Opcode.IMAGE_DATA, flags=0, sequence=1, payload=b"x" * 57).encode()


def test_icd_v013_summary_is_machine_readable() -> None:
    summary = icd_v013_summary()

    assert summary["document_version"] == "0.13"
    assert summary["commands"][0]["name"] == "PING"
    assert summary["transport"]["tx_notification_fragment_bytes"] == 20
