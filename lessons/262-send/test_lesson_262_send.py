"""Tests for Send."""

from lesson_262_send import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Send' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Send' still holds."""
    assert len(outline().splitlines()) == 3
