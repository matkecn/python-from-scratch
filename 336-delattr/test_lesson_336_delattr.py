"""Tests for Delattr."""

from lesson_336_delattr import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Delattr' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Delattr' still holds."""
    assert len(outline().splitlines()) == 3
