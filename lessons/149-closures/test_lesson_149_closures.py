"""Tests for Closures."""

from lesson_149_closures import make_counter


def test_counts_from_one() -> None:
    """The promise of lesson 'Closures' still holds."""
    assert make_counter()() == 1


def test_counts_from_a_start() -> None:
    """The promise of lesson 'Closures' still holds."""
    assert make_counter(10)() == 11
