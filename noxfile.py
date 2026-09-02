import re
import urllib.request
from pathlib import Path

import nox

nox.needs_version = ">=2026.8.10"
nox.options.sessions = ["lint", "tests"]
nox.options.default_venv_backend = "uv|virtualenv"

PYPROJECT = nox.project.load_toml("pyproject.toml")
PYTHONS = nox.project.python_versions(PYPROJECT, max_version="3.15")


@nox.session
def lint(session: nox.Session) -> None:
    """
    Run the linter.
    """
    session.install("pre-commit")
    session.run(
        "pre-commit", "run", "--all-files", "--hook-stage=manual", *session.posargs
    )


@nox.session(allow_parallel=True)
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
    license_url = (
        f"https://raw.githubusercontent.com/Kitware/CMake/v{version}/LICENSE.rst"
    )

    urllib.request.urlretrieve(cmake_url, "sphinxcontrib/moderncmakedomain/cmake.py")
    urllib.request.urlretrieve(colors_url, "sphinxcontrib/moderncmakedomain/colors.py")
    urllib.request.urlretrieve(license_url, "LICENSE.rst")

    # The upstream link to the contributor list is relative to the CMake repo.
    license_file = Path("LICENSE.rst")
    txt = license_file.read_text(encoding="utf_8")
    txt = txt.replace(
        "`Contributors <CONTRIBUTORS.rst>`_",
        "`Contributors <https://github.com/Kitware/CMake/blob/master/CONTRIBUTORS.rst>`_",
    )
    txt += "\n----\n\nSee https://cmake.org/licensing for more details\n"
    license_file.write_text(txt, encoding="utf_8")

    init_file = Path("sphinxcontrib/moderncmakedomain/__init__.py")
    txt = init_file.read_text(encoding="utf_8")
    txt_new = re.sub(r'__version__ = ".*"', f'__version__ = "{version}"', txt)
    init_file.write_text(txt_new, encoding="utf_8")


@nox.session(python=PYTHONS, allow_parallel=True)
def tests(session: nox.Session) -> None:
    """
    Run the unit and regular tests.
    """
    session.install(".[test]", silent=False)
    session.run("pytest", *session.posargs)
