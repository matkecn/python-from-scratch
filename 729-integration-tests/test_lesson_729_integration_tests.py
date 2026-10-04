"""Tests for Integration-tests."""

from lesson_729_integration_tests import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Integration-tests' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Integration-tests' still holds."""
    assert add(0, 0) == 0
