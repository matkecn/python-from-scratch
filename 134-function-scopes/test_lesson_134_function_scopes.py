"""Tests for Function-scopes."""

from lesson_134_function_scopes import area, describe


def test_computes_area() -> None:
    """The promise of lesson 'Function-scopes' still holds."""
    assert area(2.0, 3.0) == 6.0


def test_describes() -> None:
    """The promise of lesson 'Function-scopes' still holds."""
    assert describe(2.0, 3.0) == "A rectangle of 6.0 square units."
