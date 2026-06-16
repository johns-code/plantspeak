import re
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

    assert "DA14531_SDK_PATH" in content
    assert "contract-only build evidence" in content
