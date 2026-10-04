"""Tests for Itertools-tee."""

from lesson_279_itertools_tee import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-tee' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-tee' still holds."""
    assert len(outline().splitlines()) == 3
