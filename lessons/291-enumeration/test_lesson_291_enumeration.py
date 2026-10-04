"""Tests for Enumeration."""

from lesson_291_enumeration import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Enumeration' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Enumeration' still holds."""
    assert len(outline().splitlines()) == 3
