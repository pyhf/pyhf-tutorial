import os
from pathlib import Path

import nox

# Default sessions to run if no session handles are passed
nox.options.sessions = ["lock"]


DIR = Path(__file__).parent.resolve()


@nox.session(reuse_venv=True)
def lock(session: nox.Session) -> None:
    """
    Build a lock file with pip-tools

    Examples:

        $ nox --session lock
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install("--upgrade", "pip-tools")
    out = session.run(
        "cat",
        f"{DIR / 'binder' / 'requirements.txt'}",
        f"{DIR / 'book' / 'requirements.txt'}",
        external=True,
        silent=True,
    )
    intermediate_requirements = DIR / "requirements.txt"
    with open(f"{intermediate_requirements}", "w", encoding="utf8") as out_file:
        out_file.write(out.strip() + "\n")

    session.run(
        "pip-compile",
        "--resolver=backtracking",
        "--generate-hashes",
        "--output-file",
        f"{DIR / 'book' / 'requirements.lock'}",
        intermediate_requirements,
    )
    if intermediate_requirements.exists():
        intermediate_requirements.unlink()
