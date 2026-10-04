"""Tests for Itertools-groupby."""

from lesson_277_itertools_groupby import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-groupby' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-groupby' still holds."""
    assert len(outline().splitlines()) == 3
