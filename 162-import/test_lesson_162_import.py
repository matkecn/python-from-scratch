"""Tests for Import."""

from lesson_162_import import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Import' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Import' still holds."""
    assert len(outline().splitlines()) == 3
