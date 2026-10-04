"""Tests for Python REPL."""

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
