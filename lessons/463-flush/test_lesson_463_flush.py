"""Tests for Flush."""

from lesson_463_flush import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Flush' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Flush' still holds."""
    assert len(outline().splitlines()) == 3
