"""Tests for Itertools-count."""

from lesson_273_itertools_count import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-count' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-count' still holds."""
    assert len(outline().splitlines()) == 3
