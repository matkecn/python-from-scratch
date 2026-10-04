"""Tests for Global-variables."""

from lesson_136_global_variables import make_greeting, swap


def test_greets() -> None:
    """The promise of lesson 'Global-variables' still holds."""
    assert make_greeting("Ada") == "Hello, Ada!"


def test_swaps() -> None:
    """The promise of lesson 'Global-variables' still holds."""
    assert swap(1, 2) == (2, 1)


def test_swapping_twice_is_safe() -> None:
    """The promise of lesson 'Global-variables' still holds."""
    assert swap(*swap(1, 2)) == (1, 2)
