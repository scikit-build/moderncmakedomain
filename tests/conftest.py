import pytest

from pathlib import Path

pytest_plugins = 'sphinx.testing.fixtures'

@pytest.fixture(scope="session")
def rootdir():
    return Path(__file__).parent.absolute() / "roots"
