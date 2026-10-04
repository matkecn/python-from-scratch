"""Tests for __del__."""

from lesson_238_del import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson '__del__' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson '__del__' still holds."""
    assert len(outline().splitlines()) == 3
