"""Tests for Itertools-repeat."""

from lesson_272_itertools_repeat import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-repeat' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-repeat' still holds."""
    assert len(outline().splitlines()) == 3
