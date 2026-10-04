"""Tests for Build-your-own-orm."""

from lesson_997_build_your_own_orm import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-orm' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-orm' still holds."""
    assert len(outline().splitlines()) == 3
