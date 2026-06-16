from plantspeak.cli import load_requirements


def test_requirements_are_packaged() -> None:
    requirements = load_requirements()
    assert len(requirements) == 14
    assert all(requirement["id"].startswith("SW-") for requirement in requirements)
    assert all(requirement["acceptance_criteria"] for requirement in requirements)
