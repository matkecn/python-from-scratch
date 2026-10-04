"""Running Python.

Three doors into Python: a file, a single line, or the interactive prompt.

Run me:
    python 006-running-python/lesson_006_running_python.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT = '"""A tiny script."""\n\nprint("the script ran")\n'


def run_line(source: str) -> str:
    """Run one line of Python and return what it printed.

    Args:
        source: The code to run.

    Returns:
        The output, without the final newline.

    Raises:
        subprocess.CalledProcessError: If the code fails.

    Examples:
        >>> run_line("print(6 * 7)")
        '42'
    """
    finished = subprocess.run(
        [sys.executable, "-c", source],
        capture_output=True,
        text=True,
        check=True,
    )
    return finished.stdout.strip()


def write_script(path: str) -> Path:
    """Write a tiny script to disk.

    Args:
        path: Where to write it.

    Returns:
        The path that was written.
    """
    target = Path(path)
    target.write_text(SCRIPT, encoding="utf-8")
    return target


def run_script(path: str) -> str:
    """Run a script file and return what it printed.

    Args:
        path: The script to run.

    Returns:
        The output, without the final newline.

    Raises:
        subprocess.CalledProcessError: If the script fails.

    Examples:
        >>> import tempfile, os
        >>> folder = tempfile.mkdtemp()
        >>> target = write_script(os.path.join(folder, "tiny.py"))
        >>> run_script(str(target))
        'the script ran'
    """
    finished = subprocess.run(
        [sys.executable, path],
        capture_output=True,
        text=True,
        check=True,
    )
    return finished.stdout.strip()


def main() -> None:
    """Show all three ways to run Python."""
    import tempfile
    from pathlib import Path as RealPath

    print(f"one line says: {run_line('print(1 + 1)')}")
    target = write_script(str(RealPath(tempfile.mkdtemp()) / "demo.py"))
    print(f"the file says: {run_script(str(target))}")


if __name__ == "__main__":
    main()
