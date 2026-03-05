from importlib.metadata import version

import pytest

sphinx_vesion = tuple(int(d) for d in version("sphinx").split(".")[:2])

pytest_plugins = "sphinx.testing.fixtures"

if sphinx_vesion < (7, 3):
    from sphinx.testing.path import path

    @pytest.fixture(scope="session")
    def rootdir():
        return path(__file__).parent.abspath() / "roots"
else:
    from pathlib import Path

    @pytest.fixture(scope="session")
    def rootdir():
        return Path(__file__).parent.absolute() / "roots"
