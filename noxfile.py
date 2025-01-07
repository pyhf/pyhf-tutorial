import os
from pathlib import Path

import nox

# Default sessions to run if no session handles are passed
nox.options.sessions = ["lock"]


DIR = Path(__file__).parent.resolve()


@nox.session(reuse_venv=True)
def lock(session: nox.Session) -> None:
    """
    Build a lock file with uv pip compile

    Examples:

        $ nox --session lock
    """
    session.install("--upgrade", "uv")
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
        "uv",
        "pip",
        "compile",
        "--generate-hashes",
        "--output-file=book/requirements.lock",
        intermediate_requirements.name,
    )
    if intermediate_requirements.exists():
        intermediate_requirements.unlink()


@nox.session(venv_backend="none")
def docker(session: nox.Session) -> None:
    """
    Build a lock file with uv pip compile using Docker

    Examples:

        $ nox --session docker
    """
    session.run(
        "bash",
        "lock.sh",
        external=True,
    )
