"""Tests for Formatters."""

from lesson_595_formatters import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Formatters' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Formatters' still holds."""
    assert len(outline().splitlines()) == 3
