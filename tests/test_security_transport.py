import pytest

from plantspeak.transport import ICDFrame, MockTransport, TransportError, TransportErrorCode


def test_malformed_transport_payload_does_not_dispatch() -> None:
    transport = MockTransport()

    with pytest.raises(TransportError) as excinfo:
        transport.request(b'{"command": "describe-icd", "payload": []}')

    assert excinfo.value.code == TransportErrorCode.MALFORMED_FRAME
    assert transport.sent == []


def test_unsupported_transport_command_does_not_record_successful_side_effect() -> None:
    transport = MockTransport()
    frame = ICDFrame(command="unsupported", payload={}, correlation_id="bad")

    with pytest.raises(TransportError) as excinfo:
        transport.request(frame.encode())

    assert excinfo.value.code == TransportErrorCode.UNSUPPORTED_COMMAND
    assert transport.sent == [frame]
