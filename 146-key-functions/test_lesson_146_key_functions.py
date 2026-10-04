"""Tests for Key-functions."""

from lesson_146_key_functions import area, describe


def test_computes_area() -> None:
    """The promise of lesson 'Key-functions' still holds."""
    assert area(2.0, 3.0) == 6.0


def test_describes() -> None:
    """The promise of lesson 'Key-functions' still holds."""
    assert describe(2.0, 3.0) == "A rectangle of 6.0 square units."
