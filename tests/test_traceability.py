from plantspeak.requirements import ordered_requirement_ids, requirement_by_id
from plantspeak.trace import build_requirement_contracts, trace_matrix, validate_trace_matrix


def test_trace_matrix_has_no_dangling_requirement_links() -> None:
    assert validate_trace_matrix() == []

    requirement_ids = ordered_requirement_ids()
    contract_ids = [contract.requirement_id for contract in build_requirement_contracts()]
    matrix_ids = [row["requirement_id"] for row in trace_matrix()]

    assert contract_ids == requirement_ids
    assert matrix_ids == requirement_ids


def test_trace_rows_link_requirements_to_code_tests_and_evidence() -> None:
    for row in trace_matrix():
        requirement = requirement_by_id(row["requirement_id"])
        assert requirement["acceptance_criteria"]
        assert row["issue_number"]
        assert row["command"]
        assert row["code_modules"]
        assert row["unit_tests"]
        assert row["integration_tests"]
        assert row["system_tests"]
        assert row["acceptance_tests"]
        assert row["evidence_ids"]
