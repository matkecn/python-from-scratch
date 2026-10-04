"""Tests for UTF-16."""

from lesson_113_utf16 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'UTF-16' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'UTF-16' still holds."""
    assert len(outline().splitlines()) == 3
