from plantspeak.requirements import load_issue_links, load_requirements, requirement_ids


def test_requirements_and_issues_are_packaged() -> None:
    requirements = load_requirements()
    issues = load_issue_links()
    assert len(requirements) == 14
    assert len(issues) == 14
    assert "SW-001" in requirement_ids()
    assert "SW-014" in requirement_ids()
    assert all(requirement["acceptance_criteria"] for requirement in requirements)
