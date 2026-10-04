"""Tests for Test-cases."""

from lesson_712_test_cases import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Test-cases' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Test-cases' still holds."""
    assert add(0, 0) == 0
