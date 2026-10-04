"""Tests for Function-factories."""

from lesson_150_function_factories import area, describe


def test_computes_area() -> None:
    """The promise of lesson 'Function-factories' still holds."""
    assert area(2.0, 3.0) == 6.0


def test_describes() -> None:
    """The promise of lesson 'Function-factories' still holds."""
    assert describe(2.0, 3.0) == "A rectangle of 6.0 square units."
