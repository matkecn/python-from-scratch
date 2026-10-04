"""Hand written lessons 001 to 010: getting started with Python.

Each entry in :data:`LESSONS` is the full content of one lesson directory.
"""

from __future__ import annotations

from lesson_model import Lesson

__all__ = ["LESSONS"]


def lesson(
    blurb: str,
    points: tuple[str, ...],
    source: str,
    tests: str,
    practice: tuple[str, ...] = (),
    glossary: tuple[tuple[str, str], ...] = (),
    read_more: tuple[str, ...] = (),
) -> Lesson:
    """Return a hand written lesson.

    Args:
        blurb: One friendly sentence.
        points: Bullets for the "You will learn" section.
        source: The whole example module.
        tests: The whole test module.
        practice: Notebook and README exercises.
        glossary: Words to remember.
        read_more: Extra documentation links.

    Returns:
        A lesson ready to render.
    """
    return Lesson(
        blurb=blurb,
        points=points,
        source=source,
        tests=tests,
        practice=practice,
        glossary=glossary,
        read_more=read_more,
    )


LESSONS: dict[int, Lesson] = {
    1: lesson(
        blurb="Three commands and you are ready to write Python.",
        points=(
            "Check that Python is installed",
            "Read your version as two numbers",
            "Know which version this course needs",
        ),
        glossary=(
            ("interpreter", "The program that reads and runs your Python code"),
            ("version", "The number that says which release you have"),
        ),
        source='''"""Getting started.

Three commands and you are ready to write Python.

Run me:
    python 001-getting-started/lesson_001_getting_started.py
"""

from __future__ import annotations

import sys

NEEDED = (3, 11)


def version_number() -> tuple[int, int]:
    """Return the Python version as two plain numbers.

    Returns:
        The major and minor version, for example ``(3, 12)``.

    Examples:
        >>> version = version_number()
        >>> len(version)
        2
    """
    return sys.version_info.major, sys.version_info.minor


def is_supported() -> bool:
    """Say whether this Python is new enough for the course.

    Returns:
        ``True`` when the version is 3.11 or newer.

    Examples:
        >>> is_supported() == (version_number() >= (3, 11))
        True
    """
    return version_number() >= NEEDED


def version_text() -> str:
    """Return a friendly one line description of this Python.

    Returns:
        Text such as ``"Python 3.12.0 is ready"``.

    Examples:
        >>> version_text().startswith("Python 3")
        True
    """
    full = ".".join(str(part) for part in sys.version_info[:3])
    if is_supported():
        return f"Python {full} is ready"
    return f"Python {full} is too old, we need {NEEDED[0]}.{NEEDED[1]} or newer"


def main() -> None:
    """Print what we found."""
    print(version_text())


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Getting started."""

from lesson_001_getting_started import is_supported, version_number, version_text


def test_version_has_two_numbers() -> None:
    """The version comes back as two whole numbers."""
    major, minor = version_number()
    assert isinstance(major, int)
    assert isinstance(minor, int)


def test_supported_matches_the_version() -> None:
    """We agree with ourselves about which versions are new enough."""
    assert is_supported() == (version_number() >= (3, 11))


def test_version_text_starts_with_python() -> None:
    """The friendly line always starts with the word Python."""
    assert version_text().startswith("Python 3")
''',
        practice=(
            "Print the version on your own machine and compare it with a friend.",
            "Change `NEEDED` to `(3, 99)` and watch `version_text` complain.",
        ),
    ),
    2: lesson(
        blurb="Python is a language, and it is also the program that runs it.",
        points=(
            "Tell the language from the program that runs it",
            "Read the implementation and the version",
            "See that your code is turned into bytecode first",
        ),
        glossary=(
            ("CPython", "The most common Python, written in C"),
            ("bytecode", "A small set of instructions Python runs quickly"),
        ),
        source='''"""What is Python.

Python is two things: a language you write, and a program that runs it.

Run me:
    python 002-what-is-python/lesson_002_what_is_python.py
"""

from __future__ import annotations

import platform
import sys


def implementation() -> str:
    """Return the name of the Python running this code.

    Returns:
        Usually ``"CPython"``.

    Examples:
        >>> isinstance(implementation(), str)
        True
    """
    return platform.python_implementation()


def python_version() -> str:
    """Return the full version, such as ``"3.12.0"``.

    Returns:
        The version as text.
    """
    return platform.python_version()


def runs_bytecode() -> bool:
    """Say whether Python turns source into bytecode before running it.

    Returns:
        ``True`` for CPython, which caches compiled code.

    Examples:
        >>> runs_bytecode() == (implementation() == "CPython")
        True
    """
    return implementation() == "CPython"


def summary() -> str:
    """Return one sentence describing this Python.

    Returns:
        A short summary you could read out loud.
    """
    return f"{implementation()} {python_version()} runs bytecode: {runs_bytecode()}"


def main() -> None:
    """Print what we found."""
    print(summary())
    print(f"running on {sys.platform}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for What is Python."""

from lesson_002_what_is_python import implementation, python_version, runs_bytecode, summary


def test_implementation_is_text() -> None:
    """The implementation comes back as text."""
    assert isinstance(implementation(), str)
    assert implementation()


def test_version_has_three_parts() -> None:
    """The version reads like 3.12.0."""
    assert python_version().count(".") == 2


def test_bytecode_matches_the_implementation() -> None:
    """Only CPython, in this course, runs bytecode."""
    assert runs_bytecode() == (implementation() == "CPython")


def test_summary_mentions_python() -> None:
    """The summary always says the word Python."""
    assert "CPython" in summary() or "Python" in summary()
''',
        practice=(
            "Find out which Python your friend uses and compare notes.",
            "Use `sys.executable` to print the exact program that is running your code.",
        ),
    ),
    3: lesson(
        blurb="Find the Python program on your computer and check it works.",
        points=(
            "Use `shutil.which` to look for a program",
            "Fall back to the running interpreter",
            "Report a clear yes or no",
        ),
        glossary=(
            ("PATH", "The list of folders your computer searches for programs"),
            ("`python3`", "The usual name for Python on macOS and Linux"),
        ),
        source='''"""Installation.

Is Python installed? This lesson asks the computer instead of guessing.

Run me:
    python 003-installation/lesson_003_installation.py
"""

from __future__ import annotations

import shutil
import sys


def find_python() -> str:
    """Return the path of a Python program on this computer.

    Returns:
        The path of ``python3``, or the interpreter running this code.

    Examples:
        >>> bool(find_python())
        True
    """
    return shutil.which("python3") or sys.executable


def is_installed() -> bool:
    """Say whether a Python program can be found.

    Returns:
        ``True`` when Python is ready to use.
    """
    return bool(find_python())


def check() -> str:
    """Return a short report about this computer.

    Returns:
        A line a beginner can read without panic.
    """
    if not is_installed():
        return "Python is missing. Install it from python.org and try again."
    return f"Python found at {find_python()}"


def main() -> None:
    """Print the report."""
    print(check())


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Installation."""

from lesson_003_installation import check, find_python, is_installed


def test_python_can_be_found() -> None:
    """There is always a Python to run these tests."""
    assert find_python()


def test_installed_agrees_with_find_python() -> None:
    """We do not contradict ourselves."""
    assert is_installed() == bool(find_python())


def test_check_mentions_the_path() -> None:
    """The report shows where Python lives."""
    assert find_python() in check()
''',
        practice=(
            "Run `python3 --version` in your terminal and compare it with `check()`.",
            "Use `shutil.which` to find `git` the same way.",
        ),
    ),
    4: lesson(
        blurb="Python versions look like 3.12. Learn to read and compare them.",
        points=(
            "Read a version string as three numbers",
            "Compare versions without guessing",
            "Know that Python 2 is history",
        ),
        glossary=(
            ("major version", "The first number, the big release"),
            ("minor version", "The second number, the small release"),
        ),
        source='''"""Python versions.

Versions are written like ``3.12.1``: big number, small number, patch number.

Run me:
    python 004-python-versions/lesson_004_python_versions.py
"""

from __future__ import annotations

OLDEST = (3, 11)


def parse_version(text: str) -> tuple[int, int, int]:
    """Turn version text into three numbers.

    Args:
        text: A version such as ``"3.12.1"`` or ``"3.12"``.

    Returns:
        The major, minor and patch numbers, filling in zeros when missing.

    Raises:
        ValueError: If the text does not start with a number.

    Examples:
        >>> parse_version("3.12.1")
        (3, 12, 1)
        >>> parse_version("3.12")
        (3, 12, 0)
    """
    parts = text.strip().split(".")
    try:
        numbers = [int(part) for part in parts[:3]]
    except ValueError as error:
        raise ValueError(f"not a version: {text!r}") from error
    while len(numbers) < 3:
        numbers.append(0)
    return numbers[0], numbers[1], numbers[2]


def compare(first: str, second: str) -> int:
    """Compare two version strings.

    Args:
        first: The version on the left.
        second: The version on the right.

    Returns:
        ``-1`` when first is older, ``0`` when they match, ``1`` when first is newer.

    Examples:
        >>> compare("3.11.0", "3.12.0")
        -1
        >>> compare("3.12.0", "3.12.0")
        0
    """
    left = parse_version(first)
    right = parse_version(second)
    if left < right:
        return -1
    if left > right:
        return 1
    return 0


def needs_upgrade(text: str) -> bool:
    """Say whether a version is too old for this course.

    Args:
        text: The version to check.

    Returns:
        ``True`` when the course needs a newer Python.

    Examples:
        >>> needs_upgrade("3.8.10")
        True
        >>> needs_upgrade("3.13.0")
        False
    """
    major, minor, _patch = parse_version(text)
    return (major, minor) < OLDEST


def main() -> None:
    """Compare two versions out loud."""
    print(f"3.10.0 versus 3.12.0 gives {compare('3.10.0', '3.12.0')}")
    print(f"do we need an upgrade? {needs_upgrade('3.9.1')}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Python versions."""

import pytest

from lesson_004_python_versions import compare, needs_upgrade, parse_version


def test_parses_three_numbers() -> None:
    """A full version gives three numbers."""
    assert parse_version("3.12.1") == (3, 12, 1)


def test_missing_patch_becomes_zero() -> None:
    """A short version is padded with zeros."""
    assert parse_version("3.12") == (3, 12, 0)


def test_rejects_nonsense() -> None:
    """Text that is not a version is refused."""
    with pytest.raises(ValueError):
        parse_version("newest")


def test_compares_versions() -> None:
    """Older is minus one, newer is plus one, equal is zero."""
    assert compare("3.11.0", "3.12.0") == -1
    assert compare("3.12.0", "3.12.0") == 0
    assert compare("3.13.0", "3.12.0") == 1


def test_knows_what_is_too_old() -> None:
    """Python 2 and early Python 3 are too old."""
    assert needs_upgrade("3.8.10") is True
    assert needs_upgrade("2.7.18") is True
    assert needs_upgrade("3.13.0") is False
''',
        practice=(
            "Write `newer(first, second)` that returns the newer of two versions.",
            "Check the versions of five websites and find the oldest one.",
        ),
    ),
    5: lesson(
        blurb="The interpreter is the program that actually runs your code.",
        points=(
            "Find the interpreter with `sys.executable`",
            "Hand a line of code to a brand new Python",
            "Read back exactly what it printed",
        ),
        glossary=(
            ("subprocess", "The standard library way to start another program"),
            ("stdout", "The normal output a program prints"),
        ),
        source='''"""Python interpreter.

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
''',
        tests='''"""Tests for Python interpreter."""

from lesson_005_python_interpreter import interpreter_path, run_expression


def test_interpreter_path_exists() -> None:
    """The interpreter has a path we can point at."""
    assert interpreter_path()


def test_runs_a_print() -> None:
    """A brand new interpreter can add numbers."""
    assert run_expression("print(2 + 2)") == "4"


def test_runs_a_string() -> None:
    """It can also print text."""
    assert run_expression("print('hello'.upper())") == "HELLO"
''',
        practice=(
            "Use `run_expression` to ask a new Python for `sum(range(100))`.",
            "Try running code that fails and read the error message.",
        ),
    ),
    6: lesson(
        blurb="Three ways to run Python: a file, a line, or the prompt.",
        points=(
            "Run a whole file with `python file.py`",
            "Run one line with `python -c`",
            "Keep a tiny script and run it again and again",
        ),
        glossary=(
            ("script", "A file of Python instructions you can run"),
            ("argument", "A value you hand to a program"),
        ),
        source='''"""Running Python.

Three doors into Python: a file, a single line, or the interactive prompt.

Run me:
    python 006-running-python/lesson_006_running_python.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT = '"""A tiny script."""\\n\\nprint("the script ran")\\n'


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
''',
        tests='''"""Tests for Running Python."""

from lesson_006_running_python import run_line, run_script, write_script


def test_runs_a_single_line() -> None:
    """One line of code runs and prints."""
    assert run_line("print(6 * 7)") == "42"


def test_a_written_script_runs(tmp_path) -> None:
    """A file we write ourselves can be run."""
    target = write_script(str(tmp_path / "tiny.py"))
    assert target.exists()


def test_running_a_script_prints_its_line(tmp_path) -> None:
    """The script says hello when it runs."""
    target = write_script(str(tmp_path / "tiny.py"))
    assert run_script(str(target)) == "the script ran"
''',
        practice=(
            "Save your own `first.py` and run it with `python first.py`.",
            "Run the same script twice and notice nothing changes.",
        ),
    ),
    7: lesson(
        blurb="The REPL is a Python prompt that answers straight away.",
        points=(
            "Know the four parts of the prompt",
            "Try an expression and see the value",
            "Keep a useful line in your history",
        ),
        glossary=(
            ("REPL", "Read, Evaluate, Print, Loop: the interactive prompt"),
            ("expression", "A piece of code that produces a value"),
        ),
        source='''"""Python REPL.

Type ``python3`` and Python waits for you. That waiting prompt is the REPL.

Run me:
    python 007-python-repl/lesson_007_python_repl.py
"""

from __future__ import annotations

PARTS = ("read", "evaluate", "print", "loop")


def evaluate(expression: str) -> object:
    """Work out the value of a small expression.

    Only use this with code you trust. It runs the text as Python.

    Args:
        expression: The expression, such as ``"2 ** 10"``.

    Returns:
        Whatever the expression produced.

    Examples:
        >>> evaluate("2 ** 10")
        1024
        >>> evaluate("'py' + 'thon'")
        'python'
    """
    return eval(expression, {"__builtins__": {}}, {})  # noqa: S307


def describe(expression: str) -> str:
    """Return an expression's value together with its type.

    Args:
        expression: The expression to look at.

    Returns:
        Text such as ``"1024 (int)"``.

    Examples:
        >>> describe("2 + 2")
        '4 (int)'
    """
    value = evaluate(expression)
    return f"{value!r} ({type(value).__name__})"


def explain() -> str:
    """Return one line explaining what the REPL stands for.

    Returns:
        The four steps, in order.

    Examples:
        >>> explain()
        'read, evaluate, print, loop'
    """
    return ", ".join(PARTS)


def main() -> None:
    """Try a few expressions."""
    print(explain())
    for expression in ("2 + 2", "2 ** 10", "'py' + 'thon'", "[1, 2, 3]"):
        print(f"{expression:>14}  ->  {describe(expression)}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Python REPL."""

import pytest

from lesson_007_python_repl import PARTS, describe, evaluate, explain


def test_evaluate_arithmetic() -> None:
    """The prompt does maths for us."""
    assert evaluate("2 ** 10") == 1024


def test_evaluate_text() -> None:
    """It also joins strings."""
    assert evaluate("'py' + 'thon'") == "python"


def test_describe_includes_the_type() -> None:
    """We can see the type as well as the value."""
    assert describe("2 + 2") == "4 (int)"


def test_explain_lists_four_parts() -> None:
    """Read, evaluate, print, loop."""
    assert explain() == "read, evaluate, print, loop"
    assert len(PARTS) == 4


def test_evaluate_refuses_to_see_builtins() -> None:
    """Our sandbox has no built in functions, which keeps it safe."""
    with pytest.raises(NameError):
        evaluate("print(1)")
''',
        practice=(
            "Start the REPL with `python3` and try `2 ** 100`.",
            "Find the difference between `2/1` and `2//1` in the prompt.",
        ),
    ),
    8: lesson(
        blurb="Python files are plain text. Create one, read it, run it.",
        points=(
            "Write a file with `Path.write_text`",
            "Read it back line by line",
            "Keep `.py` at the end of the name",
        ),
        glossary=(
            (".py file", "A plain text file of Python code"),
            ("text mode", "Reading or writing letters, not bytes"),
        ),
        source='''"""Python files.

A Python program is a text file with a ``.py`` ending. That is all it is.

Run me:
    python 008-python-files/lesson_008_python_files.py
"""

from __future__ import annotations

from pathlib import Path


def write_script(path: str, lines: list[str]) -> int:
    """Write some lines into a Python file.

    Args:
        path: Where to write the file.
        lines: The lines to write.

    Returns:
        The number of lines written.
    """
    text = "\\n".join(lines) + "\\n"
    Path(path).write_text(text, encoding="utf-8")
    return len(lines)


def read_script(path: str) -> list[str]:
    """Read a Python file back line by line.

    Args:
        path: The file to read.

    Returns:
        The lines, without their line endings.
    """
    return Path(path).read_text(encoding="utf-8").splitlines()


def count_lines(path: str) -> int:
    """Count the lines in a file.

    Args:
        path: The file to count.

    Returns:
        How many lines it holds.
    """
    return len(read_script(path))


def is_python_file(path: str) -> bool:
    """Say whether a name looks like a Python file.

    Args:
        path: The file name to check.

    Returns:
        ``True`` when the name ends with ``.py``.

    Examples:
        >>> is_python_file("game.py")
        True
        >>> is_python_file("game.txt")
        False
    """
    return path.endswith(".py")


def main() -> None:
    """Make a file, read it back, then delete it."""
    import tempfile
    from pathlib import Path as RealPath

    target = str(RealPath(tempfile.mkdtemp()) / "demo.py")
    write_script(target, ["print('hi')", "print('bye')"])
    print(read_script(target))
    print(f"{count_lines(target)} lines, python file: {is_python_file(target)}")
    RealPath(target).unlink()


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Python files."""

from lesson_008_python_files import count_lines, is_python_file, read_script, write_script


def test_writes_a_file(tmp_path) -> None:
    """The file lands on disk with the lines we gave it."""
    target = str(tmp_path / "demo.py")
    assert write_script(target, ["print('hi')"]) == 1
    assert (tmp_path / "demo.py").exists()


def test_reads_it_back(tmp_path) -> None:
    """What we wrote is what we read."""
    target = str(tmp_path / "demo.py")
    write_script(target, ["one", "two", "three"])
    assert read_script(target) == ["one", "two", "three"]


def test_counts_lines(tmp_path) -> None:
    """Counting lines agrees with reading them."""
    target = str(tmp_path / "demo.py")
    write_script(target, ["a", "b"])
    assert count_lines(target) == 2


def test_recognises_python_files() -> None:
    """Only names ending in .py count."""
    assert is_python_file("game.py") is True
    assert is_python_file("game.txt") is False
''',
        practice=(
            "Create `my_first.py` in your text editor and run it.",
            "Change the file name and watch `is_python_file` notice.",
        ),
    ),
    9: lesson(
        blurb="Comments are notes for humans. Python ignores them.",
        points=(
            "Write a note with `#`",
            "Know that a docstring is a comment with power",
            "See why comments should say why, not what",
        ),
        glossary=(
            ("comment", "A note for people that Python skips"),
            ("docstring", "The first string in a file or function"),
        ),
        source='''"""Comments.

A comment starts with ``#`` and ends at the end of the line. Python never
runs it. People do.

Run me:
    python 009-comments/lesson_009_comments.py
"""

from __future__ import annotations

COMMENT = "#"


def is_comment(line: str) -> bool:
    """Say whether a line is only a comment.

    Args:
        line: One line of code.

    Returns:
        ``True`` when the line starts with ``#``.

    Examples:
        >>> is_comment("# a note")
        True
        >>> is_comment("total = 1  # a note")
        False
    """
    return line.strip().startswith(COMMENT)


def strip_comment(line: str) -> str:
    """Remove the comment from a line of code.

    This is a simple lesson, so it removes everything after the first ``#``.
    A ``#`` inside a string is left alone by Python but not by this helper.

    Args:
        line: One line of code.

    Returns:
        The code part of the line, with spaces trimmed.

    Examples:
        >>> strip_comment("total = 1  # add one")
        'total = 1'
        >>> strip_comment("# only a note")
        ''
    """
    return line.split(COMMENT, 1)[0].strip()


def count_comments(lines: list[str]) -> int:
    """Count how many of these lines are pure comments.

    Args:
        lines: The lines to look at.

    Returns:
        The number of comment lines.

    Examples:
        >>> count_comments(["# one", "x = 1", "# two"])
        2
    """
    return sum(1 for line in lines if is_comment(line))


def why_not_what() -> str:
    """Return the rule of thumb for writing comments.

    Returns:
        A one line reminder.

    Examples:
        >>> "why" in why_not_what()
        True
    """
    return "Say why you did it. The code already says what it does."


def main() -> None:
    """Look at a few lines of commented code."""
    lines = [
        "# This file counts birds.",
        "birds = 3  # we saw three today",
        "print(birds)",
    ]
    print(f"{count_comments(lines)} pure comment lines")
    for line in lines:
        print(f"{strip_comment(line)!r}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Comments."""

from lesson_009_comments import count_comments, is_comment, strip_comment, why_not_what


def test_finds_comment_lines() -> None:
    """A line that starts with # is a comment."""
    assert is_comment("# a note") is True
    assert is_comment("   # indented note") is True


def test_code_with_a_note_is_not_a_comment_line() -> None:
    """Code followed by a note is still code."""
    assert is_comment("total = 1  # a note") is False


def test_strips_the_note() -> None:
    """What is left is the code."""
    assert strip_comment("total = 1  # add one") == "total = 1"


def test_a_whole_comment_becomes_nothing() -> None:
    """Stripping a comment line leaves an empty string."""
    assert strip_comment("# only a note") == ""


def test_counts_comments() -> None:
    """Only pure comment lines are counted."""
    assert count_comments(["# one", "x = 1", "# two"]) == 2


def test_the_rule_mentions_why() -> None:
    """Good comments explain why."""
    assert "why" in why_not_what()
''',
        practice=(
            "Take a file you wrote and delete every comment that only says what.",
            "Write a comment that explains why a strange value is needed.",
        ),
    ),
    10: lesson(
        blurb="Indentation is how Python shows which lines belong together.",
        points=(
            "Blocks start with a `:` and end when the indentation shrinks",
            "Measure indentation with `len`",
            "Keep blocks at one consistent width",
        ),
        glossary=(
            ("block", "A group of lines that belong together"),
            ("indentation", "The spaces at the start of a line"),
        ),
        source='''"""Indentation.

Python does not use braces. It uses the spaces at the start of a line. Four
spaces is the usual width.

Run me:
    python 010-indentation/lesson_010_indentation.py
"""

from __future__ import annotations

WIDTH = 4


def indent_width(line: str) -> int:
    """Return how far a line is indented.

    Args:
        line: One line of code.

    Returns:
        The number of spaces before the first real character.

    Examples:
        >>> indent_width("    print(1)")
        4
        >>> indent_width("print(1)")
        0
    """
    return len(line) - len(line.lstrip(" "))


def opens_a_block(line: str) -> bool:
    """Say whether a line starts a new block.

    Args:
        line: One line of code.

    Returns:
        ``True`` when the line ends with a colon.

    Examples:
        >>> opens_a_block("if ready:")
        True
        >>> opens_a_block("    print(1)")
        False
    """
    return line.strip().endswith(":")


def block_depth(lines: list[str]) -> int:
    """Return how deep the deepest block goes.

    Args:
        lines: The lines of code.

    Returns:
        The largest indentation found, in spaces.

    Examples:
        >>> block_depth(["if a:", "    print(1)", "    for b in c:", "        print(2)"])
        8
    """
    return max((indent_width(line) for line in lines), default=0)


def count_statements(lines: list[str]) -> int:
    """Count the lines that actually do something.

    Blank lines, comments and closing brackets do not count.

    Args:
        lines: The lines of code.

    Returns:
        The number of real statements.

    Examples:
        >>> count_statements(["x = 1", "", "# note", "print(x)"])
        2
    """
    count = 0
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if text in {"}", "]", ")"}:
            continue
        count += 1
    return count


def main() -> None:
    """Measure a small piece of indented code."""
    lines = [
        "total = 0",
        "for number in [1, 2, 3]:",
        "    total += number",
        "print(total)",
    ]
    print(f"deepest block: {block_depth(lines)} spaces")
    print(f"statements: {count_statements(lines)}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Indentation."""

from lesson_010_indentation import block_depth, count_statements, indent_width, opens_a_block


def test_measures_indentation() -> None:
    """We count the spaces at the start of a line."""
    assert indent_width("    print(1)") == 4
    assert indent_width("print(1)") == 0


def test_finds_block_openers() -> None:
    """A line ending in a colon starts a block."""
    assert opens_a_block("if ready:") is True
    assert opens_a_block("    print(1)") is False


def test_finds_the_deepest_block() -> None:
    """Nested blocks go deeper."""
    assert block_depth(["if a:", "    print(1)", "    for b in c:", "        print(2)"]) == 8


def test_empty_code_has_no_depth() -> None:
    """Nothing means nothing."""
    assert block_depth([]) == 0


def test_counts_only_real_statements() -> None:
    """Blank lines and comments are not statements."""
    assert count_statements(["x = 1", "", "# note", "print(x)"]) == 2
''',
        practice=(
            "Rewrite a four space block with two spaces and see if Python complains.",
            "Find the deepest block in a file you already wrote.",
        ),
    ),
}
