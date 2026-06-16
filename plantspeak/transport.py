from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from enum import Enum

from plantspeak.icd import COMMANDS_BY_REQUIREMENT, capability_summary


MAX_PAYLOAD_BYTES = 512


class TransportErrorCode(str, Enum):
    MALFORMED_FRAME = "malformed-frame"
    OVERSIZED_PAYLOAD = "oversized-payload"
    UNSUPPORTED_COMMAND = "unsupported-command"
    TIMEOUT = "timeout"


class TransportError(RuntimeError):
    def __init__(self, code: TransportErrorCode, message: str) -> None:
        super().__init__(message)
        self.code = code


@dataclass(frozen=True)
class ICDFrame:
    command: str
    payload: dict[str, object]
    correlation_id: str

    def encode(self) -> bytes:
        data = json.dumps(asdict(self), sort_keys=True).encode("utf-8")
        if len(data) > MAX_PAYLOAD_BYTES:
            raise TransportError(TransportErrorCode.OVERSIZED_PAYLOAD, "frame payload exceeds maximum size")
        return data

    @staticmethod
    def decode(raw: bytes) -> "ICDFrame":
        if len(raw) > MAX_PAYLOAD_BYTES:
            raise TransportError(TransportErrorCode.OVERSIZED_PAYLOAD, "frame payload exceeds maximum size")
        try:
            data = json.loads(raw.decode("utf-8"))
            command = data["command"]
            payload = data["payload"]
            correlation_id = data["correlation_id"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise TransportError(TransportErrorCode.MALFORMED_FRAME, "frame is not valid ICD JSON") from exc
        if not isinstance(command, str) or not isinstance(payload, dict) or not isinstance(correlation_id, str):
            raise TransportError(TransportErrorCode.MALFORMED_FRAME, "frame fields have invalid types")
        return ICDFrame(command=command, payload=payload, correlation_id=correlation_id)


@dataclass(frozen=True)
class ICDResponse:
    correlation_id: str
    status: str
    payload: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def dispatch_frame(frame: ICDFrame) -> ICDResponse:
    commands = set(COMMANDS_BY_REQUIREMENT.values())
    if frame.command not in commands:
        raise TransportError(TransportErrorCode.UNSUPPORTED_COMMAND, f"unsupported command: {frame.command}")
    if frame.command == "describe-icd":
        return ICDResponse(frame.correlation_id, "ok", {"capabilities": capability_summary()})
    return ICDResponse(
        frame.correlation_id,
        "deferred",
        {"command": frame.command, "reason": "command contract exists; execution is handled by staged implementation"},
    )


class MockTransport:
    def __init__(self, timeout: bool = False) -> None:
        self.timeout = timeout
        self.sent: list[ICDFrame] = []

    def request(self, raw: bytes) -> ICDResponse:
        if self.timeout:
            raise TransportError(TransportErrorCode.TIMEOUT, "mock transport timeout")
        frame = ICDFrame.decode(raw)
        self.sent.append(frame)
        return dispatch_frame(frame)
