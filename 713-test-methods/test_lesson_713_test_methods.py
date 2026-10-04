"""Tests for Test-methods."""

from lesson_713_test_methods import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Test-methods' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Test-methods' still holds."""
    assert add(0, 0) == 0
