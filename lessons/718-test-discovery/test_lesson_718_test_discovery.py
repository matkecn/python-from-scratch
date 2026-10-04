"""Tests for Test-discovery."""

from lesson_718_test_discovery import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Test-discovery' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Test-discovery' still holds."""
    assert add(0, 0) == 0
