from plantspeak.contracts import RequirementContract, validate_requirement_contract
from plantspeak.trace import build_requirement_contracts


def test_requirement_contracts_are_complete() -> None:
    contracts = build_requirement_contracts()

    assert len(contracts) == 14
    for contract in contracts:
        assert isinstance(contract, RequirementContract)
        assert validate_requirement_contract(contract) == []
        assert contract.command
        assert contract.code_modules
        assert contract.unit_tests
        assert contract.system_tests
        assert contract.acceptance_tests
        assert contract.evidence_ids


def test_contracts_name_stage_and_evidence_for_each_requirement() -> None:
    contracts = {contract.requirement_id: contract for contract in build_requirement_contracts()}

    assert contracts["SW-001"].first_stage == "S1"
    assert contracts["SW-006"].first_stage == "S2"
    assert "ST-004" in contracts["SW-006"].system_tests
    assert "AT-004" in contracts["SW-014"].acceptance_tests
