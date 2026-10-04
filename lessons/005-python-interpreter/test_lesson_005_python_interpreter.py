"""Tests for Python interpreter."""

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
