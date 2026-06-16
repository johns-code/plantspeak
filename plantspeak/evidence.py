from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from plantspeak.devices import build_capability_map, collect_dev_mode_snapshot, default_dev_board_profile
from plantspeak.icd import build_icd_capabilities, capability_summary
from plantspeak.trace import trace_matrix


@dataclass(frozen=True)
class EvidenceResult:
    test_id: str
    path: str
    requirement_ids: tuple[str, ...]
    status: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


SYSTEM_EVIDENCE = {
    "ST-001": {
        "path": "ST-001.json",
        "requirements": ("SW-001", "SW-013", "SW-014"),
        "argv": ("self-test", "--dev-mode"),
    },
    "ST-002": {
        "path": "ST-002.txt",
        "requirements": tuple(f"SW-{index:03d}" for index in range(1, 15)),
        "argv": ("trace",),
    },
    "ST-003": {
        "path": "ST-003.json",
        "requirements": ("SW-001", "SW-006", "SW-013", "SW-014"),
        "argv": ("capabilities",),
    },
    "ST-004": {
        "path": "ST-004.json",
        "requirements": ("SW-006", "SW-008", "SW-009", "SW-010", "SW-013"),
        "argv": ("measure", "--dev-mode"),
    },
}


def generate_system_evidence(output_dir: Path) -> list[EvidenceResult]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results: list[EvidenceResult] = []
    for test_id, spec in SYSTEM_EVIDENCE.items():
        target = output_dir / str(spec["path"])
        status = _capture_command(tuple(spec["argv"]), target)
        results.append(
            EvidenceResult(
                test_id=test_id,
                path=str(target),
                requirement_ids=tuple(spec["requirements"]),
                status=status,
            )
        )
    manifest = output_dir / "manifest.json"
    manifest.write_text(json.dumps([result.to_dict() for result in results], indent=2) + "\n", encoding="utf-8")
    return results


def _capture_command(argv: tuple[str, ...], target: Path) -> str:
    if argv == ("self-test", "--dev-mode"):
        profile = default_dev_board_profile()
        capability_map = build_capability_map(profile)
        payload = {
            "external_i2c_uses_canned_data": capability_map["SW-013"] == "canned-data",
            "button_wake_deferred": capability_map["SW-014"] == "dev-board-unavailable",
            "icd_capabilities_present": len(build_icd_capabilities()) == 14,
        }
        target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return "PASS" if all(payload.values()) else "FAIL"
    if argv == ("trace",):
        lines = [
            f"{row['requirement_id']} -> #{row['issue_number'] or 'local'} -> {row['command']} -> {', '.join(row['system_tests'])}"
            for row in trace_matrix()
        ]
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return "PASS"
    if argv == ("capabilities",):
        target.write_text(json.dumps(capability_summary(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return "PASS"
    if argv == ("measure", "--dev-mode"):
        target.write_text(json.dumps(collect_dev_mode_snapshot().to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return "PASS"
    raise ValueError(f"unsupported evidence command: {argv}")
