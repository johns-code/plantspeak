import json

from plantspeak.evidence import generate_system_evidence


def test_generate_system_evidence_creates_manifest_and_artifacts(tmp_path) -> None:
    results = generate_system_evidence(tmp_path)

    assert {result.test_id for result in results} == {"ST-001", "ST-002", "ST-003", "ST-004"}
    assert all(result.status == "PASS" for result in results)
    assert (tmp_path / "ST-001.json").exists()
    assert (tmp_path / "ST-002.txt").exists()
    assert (tmp_path / "ST-003.json").exists()
    assert (tmp_path / "ST-004.json").exists()
    assert (tmp_path / "manifest.json").exists()


def test_generated_evidence_is_requirement_linked_and_parseable(tmp_path) -> None:
    generate_system_evidence(tmp_path)

    manifest = json.loads((tmp_path / "manifest.json").read_text(encoding="utf-8"))
    assert all(item["requirement_ids"] for item in manifest)
    assert json.loads((tmp_path / "ST-001.json").read_text(encoding="utf-8"))["icd_capabilities_present"] is True
    assert json.loads((tmp_path / "ST-003.json").read_text(encoding="utf-8"))["SW-001"]["command"] == "describe-icd"
    assert json.loads((tmp_path / "ST-004.json").read_text(encoding="utf-8"))["source"] == "canned-dev-mode-data"
    assert "SW-014" in (tmp_path / "ST-002.txt").read_text(encoding="utf-8")
