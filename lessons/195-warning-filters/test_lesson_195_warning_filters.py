"""Tests for Warning-filters."""

from lesson_195_warning_filters import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Warning-filters' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Warning-filters' still holds."""
    assert len(outline().splitlines()) == 3
