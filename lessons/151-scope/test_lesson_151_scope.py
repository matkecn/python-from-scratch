"""Tests for Scope."""

from lesson_151_scope import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Scope' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Scope' still holds."""
    assert len(outline().splitlines()) == 3
