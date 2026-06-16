from plantspeak.icd import build_icd_capabilities, capability_summary


def test_icd_capabilities_cover_all_software_requirements() -> None:
    capabilities = build_icd_capabilities()
    assert len(capabilities) == 14
    assert {capability.requirement_id for capability in capabilities} == {f"SW-{index:03d}" for index in range(1, 15)}


def test_icd_summary_identifies_deferred_wake_behavior() -> None:
    summary = capability_summary()
    assert summary["SW-014"]["command"] == "report-user-button-unavailable"
    assert summary["SW-014"]["implementation_status"] == "dev-board-unavailable"
