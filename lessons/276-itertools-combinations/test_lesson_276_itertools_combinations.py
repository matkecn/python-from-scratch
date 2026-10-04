"""Tests for Itertools-combinations."""

from lesson_276_itertools_combinations import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-combinations' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-combinations' still holds."""
    assert len(outline().splitlines()) == 3
