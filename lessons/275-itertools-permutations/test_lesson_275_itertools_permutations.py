"""Tests for Itertools-permutations."""

from lesson_275_itertools_permutations import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-permutations' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-permutations' still holds."""
    assert len(outline().splitlines()) == 3
