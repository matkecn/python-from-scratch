"""Tests for Iterator-challenges."""

from lesson_974_iterator_challenges import count_to, take_first


def test_counts() -> None:
    """The promise of lesson 'Iterator-challenges' still holds."""
    assert count_to(3) == 3


def test_takes_two() -> None:
    """The promise of lesson 'Iterator-challenges' still holds."""
    assert take_first([9, 8, 7], 2) == [9, 8]
