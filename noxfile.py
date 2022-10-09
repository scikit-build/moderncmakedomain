import nox
import urllib.request
import re
from pathlib import Path

nox.options.sessions = ["lint", "tests"]

ALL_PYTHONS = ["3.6", "3.7", "3.8", "3.9", "3.10", "3.11"]

@nox.session
def lint(session: nox.Session) -> None:
    """
    Run the linter.
    """
    session.install("pre-commit")
    session.run(
        "pre-commit", "run", "--all-files", "--hook-stage=manual", *session.posargs
    )


@nox.session
def build(session: nox.Session) -> None:
    """
    Build an SDist and wheel.
    """

    session.install("build")
    session.run("python", "-m", "build")


@nox.session
def update(session: nox.Session) -> None:
    """
    Get the latest (or given) version of CMake and update the copy with it.
    """

    if session.posargs:
        (version,) = session.posargs
    else:
        session.install("lastversion")
        version = session.run(
            "lastversion", "kitware/cmake", log=False, silent=True
        ).strip()
        session.log(f"CMake {version}")

    cmake_url = f"https://raw.githubusercontent.com/Kitware/CMake/v{version}/Utilities/Sphinx/cmake.py"
    colors_url = f"https://raw.githubusercontent.com/Kitware/CMake/v{version}/Utilities/Sphinx/colors.py"

    urllib.request.urlretrieve(cmake_url, "sphinxcontrib/moderncmakedomain/cmake.py")
    urllib.request.urlretrieve(colors_url, "sphinxcontrib/moderncmakedomain/colors.py")

    init_file = Path("sphinxcontrib/moderncmakedomain/__init__.py")
    txt = init_file.read_text(encoding="utf_8")
    txt_new = re.sub(r'__version__ = ".*"', f'__version__ = "{version}"', txt)
    init_file.write_text(txt_new, encoding="utf_8")


@nox.session(python=ALL_PYTHONS)
def tests(session):
    """
    Run the unit and regular tests.
    """
    session.install(".", "pytest")
    session.run("pytest", *session.posargs)
