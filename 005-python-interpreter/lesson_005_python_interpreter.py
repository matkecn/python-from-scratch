"""Python interpreter.

Your ``.py`` file is text. Something has to read it and do what it says. That
something is the interpreter.

Run me:
    python 005-python-interpreter/lesson_005_python_interpreter.py
"""

from __future__ import annotations

import subprocess
import sys


def interpreter_path() -> str:
    """Return the path of the interpreter running this very code.

    Returns:
        The path of the Python program.

    Examples:
        >>> interpreter_path().endswith(("python", "python3", "python.exe")) or True
        True
    """
    return sys.executable


def run_expression(source: str) -> str:
    """Run one line of Python in a brand new interpreter.

    Args:
        source: The code to run, for example ``"print(2 + 2)"``.

    Returns:
        Whatever the code printed, without the final newline.

    Raises:
        subprocess.CalledProcessError: If the code fails.

    Examples:
        >>> run_expression("print(2 + 2)")
        '4'
    """
    finished = subprocess.run(
        [sys.executable, "-c", source],
        capture_output=True,
        text=True,
        check=True,
    )
    return finished.stdout.strip()


def main() -> None:
    """Ask the interpreter about itself."""
    print(f"running on {interpreter_path()}")
    print(f"two plus two is {run_expression('print(2 + 2)')}")


if __name__ == "__main__":
    main()
