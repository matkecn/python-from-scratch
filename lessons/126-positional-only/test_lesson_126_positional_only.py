"""Tests for Positional-only."""

from lesson_126_positional_only import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Positional-only' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Positional-only' still holds."""
    assert len(outline().splitlines()) == 3
