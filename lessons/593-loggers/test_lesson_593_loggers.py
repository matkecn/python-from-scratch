"""Tests for Loggers."""

from lesson_593_loggers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Loggers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Loggers' still holds."""
    assert len(outline().splitlines()) == 3
