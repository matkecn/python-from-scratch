"""Tests for Getters and setters."""

from lesson_212_getters_setters import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Getters and setters' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Getters and setters' still holds."""
    assert len(outline().splitlines()) == 3
