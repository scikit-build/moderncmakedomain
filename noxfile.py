import nox
import urllib.request

nox.options.sessions = ["lint"]


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
    Get the latest (or given) version of cmake and update the copy with it.
    """

    if session.posargs:
        (version,) = session.posargs
    else:
        session.install("lastversion")
        version = session.run(
            "lastversion", "kitware/cmake", log=False, silent=True
        ).strip()

    cmake_url = f"https://raw.githubusercontent.com/Kitware/CMake/v{version}/Utilities/Sphinx/cmake.py"
    colors_url = f"https://raw.githubusercontent.com/Kitware/CMake/v{version}/Utilities/Sphinx/colors.py"

    urllib.request.urlretrieve(cmake_url, "sphinxcontrib/moderncmakedomain/cmake.py")
    urllib.request.urlretrieve(colors_url, "sphinxcontrib/moderncmakedomain/colors.py")

    session.install("bump2version")
    session.run(
        "bumpversion", "--allow-dirty", "--new-version", version, "patch", "setup.cfg"
    )
