"""Tests for Memory-layout."""

from lesson_856_memory_layout import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Memory-layout' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Memory-layout' still holds."""
    assert len(outline().splitlines()) == 3
