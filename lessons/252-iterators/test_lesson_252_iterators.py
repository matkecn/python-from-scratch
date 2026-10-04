"""Tests for Iterators."""

from lesson_252_iterators import count_to, take_first


def test_counts() -> None:
    """The promise of lesson 'Iterators' still holds."""
    assert count_to(3) == 3


def test_takes_two() -> None:
    """The promise of lesson 'Iterators' still holds."""
    assert take_first([9, 8, 7], 2) == [9, 8]
