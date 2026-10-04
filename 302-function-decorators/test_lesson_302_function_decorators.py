"""Tests for Function-decorators."""

from lesson_302_function_decorators import area, describe


def test_computes_area() -> None:
    """The promise of lesson 'Function-decorators' still holds."""
    assert area(2.0, 3.0) == 6.0


def test_describes() -> None:
    """The promise of lesson 'Function-decorators' still holds."""
    assert describe(2.0, 3.0) == "A rectangle of 6.0 square units."
