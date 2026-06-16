import pytest

from plantspeak.transport import ICDFrame, MockTransport, TransportError, TransportErrorCode, dispatch_frame


def test_transport_dispatches_describe_icd() -> None:
    frame = ICDFrame(command="describe-icd", payload={}, correlation_id="abc")

    response = MockTransport().request(frame.encode())

    assert response.correlation_id == "abc"
    assert response.status == "ok"
    assert "SW-001" in response.payload["capabilities"]


def test_transport_dispatches_deferred_known_command_without_side_effects() -> None:
    frame = ICDFrame(command="read-light-sensors", payload={}, correlation_id="measure-1")

    response = dispatch_frame(frame)

    assert response.status == "deferred"
    assert response.payload["command"] == "read-light-sensors"


@pytest.mark.parametrize("raw", [b"not-json", b"{]", b'{"command": 12, "payload": {}, "correlation_id": "x"}'])
def test_transport_rejects_malformed_payload(raw: bytes) -> None:
    with pytest.raises(TransportError) as excinfo:
        MockTransport().request(raw)

    assert excinfo.value.code == TransportErrorCode.MALFORMED_FRAME


def test_transport_rejects_oversized_payload() -> None:
    frame = ICDFrame(command="describe-icd", payload={"blob": "x" * 600}, correlation_id="big")

    with pytest.raises(TransportError) as excinfo:
        frame.encode()

    assert excinfo.value.code == TransportErrorCode.OVERSIZED_PAYLOAD


def test_transport_rejects_unsupported_command() -> None:
    frame = ICDFrame(command="erase-everything", payload={}, correlation_id="bad")

    with pytest.raises(TransportError) as excinfo:
        MockTransport().request(frame.encode())

    assert excinfo.value.code == TransportErrorCode.UNSUPPORTED_COMMAND


def test_transport_timeout_is_explicit() -> None:
    frame = ICDFrame(command="describe-icd", payload={}, correlation_id="timeout")

    with pytest.raises(TransportError) as excinfo:
        MockTransport(timeout=True).request(frame.encode())

    assert excinfo.value.code == TransportErrorCode.TIMEOUT
