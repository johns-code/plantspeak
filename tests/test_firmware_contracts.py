import re
import json
from pathlib import Path

from plantspeak.icd import COMMANDS_BY_REQUIREMENT
from plantspeak.pins import pin_map


ROOT = Path(__file__).resolve().parents[1]


def test_firmware_command_table_matches_python_icd_contract() -> None:
    content = (ROOT / "firmware" / "icd_command_table.h").read_text(encoding="utf-8")
    rows = dict(re.findall(r'\{"(SW-\d{3})", "([^"]+)"\}', content))

    assert rows == COMMANDS_BY_REQUIREMENT


def test_firmware_pin_config_matches_python_pin_contract() -> None:
    content = (ROOT / "firmware" / "pin_config.h").read_text(encoding="utf-8")
    pins = pin_map()

    assert f'"{pins["red_user_led"].pin}"' in content
    assert f'"{pins["green_user_led"].pin}"' in content
    assert f'"{pins["user_push_button"].pin}"' in content
    assert f'"{pins["en_peripherals"].pin}"' in content
    assert f'"{pins["i2c_scl"].pin}"' in content
    assert f'"{pins["i2c_sda"].pin}"' in content


def test_firmware_build_script_documents_contract_only_mode() -> None:
    content = (ROOT / "firmware" / "build.ps1").read_text(encoding="utf-8")

    assert "KEIL_UV4_PATH" in content
    assert "PLANTSPEAK_KEIL_PROJECT" in content
    assert "contract-only build evidence" in content
    assert "0 Error" in content


def test_real_board_keil_build_evidence_is_captured() -> None:
    summary = json.loads((ROOT / "docs" / "test-evidence" / "keil-da14531-build-summary.json").read_text(encoding="utf-8"))
    raw_log = (ROOT / "docs" / "test-evidence" / "keil-da14531-build-raw.log").read_text(encoding="utf-8")

    assert summary["gate"] == "keil-da14531-build"
    assert summary["status"] == "pass"
    assert summary["target"] == "DA14531"
    assert "0 Error(s)" in summary["result"]
    assert "0 Error(s)" in raw_log
    assert len(summary["outputs"]) == 3
    assert {Path(output["path"]).suffix for output in summary["outputs"]} == {".axf", ".hex", ".bin"}
    assert all(output["size_bytes"] > 0 for output in summary["outputs"])
    assert all(re.fullmatch(r"[0-9a-f]{64}", output["sha256"]) for output in summary["outputs"])


def test_jlink_probe_evidence_is_captured() -> None:
    summary = json.loads((ROOT / "docs" / "test-evidence" / "jlink-probe-summary.json").read_text(encoding="utf-8"))
    raw_log = (ROOT / "docs" / "test-evidence" / "jlink-probe-raw.log").read_text(encoding="utf-8")

    assert summary["gate"] == "jlink-emulator-probe"
    assert summary["status"] == "pass"
    assert summary["connected"] is True
    assert summary["serial_number"]
    assert "J-Link[0]" in raw_log
