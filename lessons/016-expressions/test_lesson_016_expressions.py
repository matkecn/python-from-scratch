"""Tests for Expressions."""

import pytest

from lesson_016_expressions import describe, evaluate, is_expression


def test_describe_value_and_type() -> None:
    """We show the value and the type."""
    assert describe(5) == "5 (int)"


def test_evaluate_arithmetic() -> None:
    """Expressions produce values."""
    assert evaluate("2 + 3") == 5
    assert evaluate("2 ** 8") == 256


def test_evaluate_refuses_words() -> None:
    """A name is not defined in our tiny sandbox."""
    with pytest.raises(NameError):
        evaluate("some_name")


def test_recognises_expressions() -> None:
    """A bare calculation is an expression."""
    assert is_expression("2 + 3") is True


def test_assignment_is_not_an_expression() -> None:
    """Putting a value in a name is a statement."""
    assert is_expression("total = 2 + 3") is False
