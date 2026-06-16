import os


def pytest_addoption(parser):
    parser.addoption("--target-board", action="store_true", help="Enable PlantSpeak target-board HIL tests.")


def pytest_configure(config):
    if config.getoption("--target-board"):
        os.environ["PLANTSPEAK_TARGET_BOARD"] = "1"
