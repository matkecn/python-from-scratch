"""Tests for Test-suites."""

from lesson_717_test_suites import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Test-suites' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Test-suites' still holds."""
    assert add(0, 0) == 0
