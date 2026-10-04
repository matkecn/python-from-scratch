"""Tests for Function-parameters."""

from lesson_122_function_parameters import area, describe


def test_computes_area() -> None:
    """The promise of lesson 'Function-parameters' still holds."""
    assert area(2.0, 3.0) == 6.0


def test_describes() -> None:
    """The promise of lesson 'Function-parameters' still holds."""
    assert describe(2.0, 3.0) == "A rectangle of 6.0 square units."
