"""Tests for Test-driven-development."""

from lesson_734_test_driven_development import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Test-driven-development' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Test-driven-development' still holds."""
    assert add(0, 0) == 0
