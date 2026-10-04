"""Tests for Try."""

from lesson_182_try import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Try' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Try' still holds."""
    assert len(outline().splitlines()) == 3
