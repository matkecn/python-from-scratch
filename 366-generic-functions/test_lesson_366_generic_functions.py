"""Tests for Generic-functions."""

from lesson_366_generic_functions import area, describe


def test_computes_area() -> None:
    """The promise of lesson 'Generic-functions' still holds."""
    assert area(2.0, 3.0) == 6.0


def test_describes() -> None:
    """The promise of lesson 'Generic-functions' still holds."""
    assert describe(2.0, 3.0) == "A rectangle of 6.0 square units."
