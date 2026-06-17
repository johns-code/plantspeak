import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_release_candidate_manifest_references_existing_artifacts() -> None:
    manifest = json.loads((ROOT / "docs" / "release-evidence" / "release-candidate-manifest.json").read_text(encoding="utf-8"))

    missing = [path for path in manifest["required_artifacts"] if not (ROOT / path).exists()]
    assert missing == []


def test_release_candidate_requires_remaining_target_board_validation() -> None:
    manifest = json.loads((ROOT / "docs" / "release-evidence" / "release-candidate-manifest.json").read_text(encoding="utf-8"))

    assert manifest["human_approval_required"] is True
    assert manifest["automated_gates"]["s8_keil_build_gate"] == "pass"
    assert manifest["automated_gates"]["s8_jlink_probe"] == "pass"
    assert "target-board I2C device reads" in manifest["deferred_validation"]
    assert "physical DA14531 firmware build" not in manifest["deferred_validation"]
