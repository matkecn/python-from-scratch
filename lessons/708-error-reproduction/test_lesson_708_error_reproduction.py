"""Tests for Error-reproduction."""

from lesson_708_error_reproduction import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Error-reproduction' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Error-reproduction' still holds."""
    assert len(outline().splitlines()) == 3
