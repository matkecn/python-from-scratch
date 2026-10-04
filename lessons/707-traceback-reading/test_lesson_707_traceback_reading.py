"""Tests for Traceback-reading."""

from lesson_707_traceback_reading import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Traceback-reading' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Traceback-reading' still holds."""
    assert len(outline().splitlines()) == 3
