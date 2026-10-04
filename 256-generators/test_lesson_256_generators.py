"""Tests for Generators."""

from lesson_256_generators import count_up, evens


def test_counts_up() -> None:
    """The promise of lesson 'Generators' still holds."""
    assert list(count_up(3)) == [1, 2, 3]


def test_keeps_evens() -> None:
    """The promise of lesson 'Generators' still holds."""
    assert list(evens(7)) == [0, 2, 4, 6]
