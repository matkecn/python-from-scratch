"""Tests for Small integers."""

from lesson_858_small_integers import whole_pairs, is_even


def test_counts_pairs() -> None:
    """The promise of lesson 'Small integers' still holds."""
    assert whole_pairs(7) == 3


def test_even_is_true() -> None:
    """The promise of lesson 'Small integers' still holds."""
    assert is_even(4) is True


def test_odd_is_false() -> None:
    """The promise of lesson 'Small integers' still holds."""
    assert is_even(5) is False
