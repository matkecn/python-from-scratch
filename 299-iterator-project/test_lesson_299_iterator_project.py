"""Tests for Iterator-project."""

from lesson_299_iterator_project import count_to, take_first


def test_counts() -> None:
    """The promise of lesson 'Iterator-project' still holds."""
    assert count_to(3) == 3


def test_takes_two() -> None:
    """The promise of lesson 'Iterator-project' still holds."""
    assert take_first([9, 8, 7], 2) == [9, 8]
