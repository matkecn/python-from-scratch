"""Tests for __init__."""

from lesson_237_init import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson '__init__' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson '__init__' still holds."""
    assert len(outline().splitlines()) == 3
