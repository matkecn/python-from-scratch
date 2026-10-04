"""Tests for Custom-awaitable."""

from lesson_448_custom_awaitable import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Custom-awaitable' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Custom-awaitable' still holds."""
    assert len(outline().splitlines()) == 3
