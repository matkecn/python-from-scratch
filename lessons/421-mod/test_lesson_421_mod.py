"""Tests for Mod."""

from lesson_421_mod import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Mod' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Mod' still holds."""
    assert len(outline().splitlines()) == 3
