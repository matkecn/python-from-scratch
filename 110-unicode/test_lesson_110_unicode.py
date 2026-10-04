"""Tests for Unicode."""

from lesson_110_unicode import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Unicode' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Unicode' still holds."""
    assert len(outline().splitlines()) == 3
