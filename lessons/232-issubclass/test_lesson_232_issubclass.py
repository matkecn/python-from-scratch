"""Tests for Issubclass."""

from lesson_232_issubclass import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Issubclass' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Issubclass' still holds."""
    assert len(outline().splitlines()) == 3
