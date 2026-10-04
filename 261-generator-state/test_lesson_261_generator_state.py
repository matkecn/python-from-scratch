"""Tests for Generator-state."""

from lesson_261_generator_state import count_up, evens


def test_counts_up() -> None:
    """The promise of lesson 'Generator-state' still holds."""
    assert list(count_up(3)) == [1, 2, 3]


def test_keeps_evens() -> None:
    """The promise of lesson 'Generator-state' still holds."""
    assert list(evens(7)) == [0, 2, 4, 6]
