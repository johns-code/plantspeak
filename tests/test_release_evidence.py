import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_release_candidate_manifest_references_existing_artifacts() -> None:
    manifest = json.loads((ROOT / "docs" / "release-evidence" / "release-candidate-manifest.json").read_text(encoding="utf-8"))

    missing = [path for path in manifest["required_artifacts"] if not (ROOT / path).exists()]
    assert missing == []


def test_release_candidate_keeps_target_board_validation_deferred() -> None:
    manifest = json.loads((ROOT / "docs" / "release-evidence" / "release-candidate-manifest.json").read_text(encoding="utf-8"))

    assert manifest["human_approval_required"] is True
    assert manifest["automated_gates"]["s6_hil_gate"] == "pass-with-target-board-tests-skipped"
    assert "target-board I2C device reads" in manifest["deferred_validation"]
