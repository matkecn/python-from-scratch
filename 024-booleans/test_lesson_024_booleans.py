"""Tests for Booleans."""

from lesson_024_booleans import is_odd, both_yes


def test_three_is_odd() -> None:
    """The promise of lesson 'Booleans' still holds."""
    assert is_odd(3) is True


def test_two_is_not_odd() -> None:
    """The promise of lesson 'Booleans' still holds."""
    assert is_odd(2) is False


def test_and_needs_both() -> None:
    """The promise of lesson 'Booleans' still holds."""
    assert both_yes(True, True) is True
