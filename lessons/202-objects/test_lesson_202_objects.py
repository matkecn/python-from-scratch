"""Tests for Objects."""

from lesson_202_objects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Objects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Objects' still holds."""
    assert len(outline().splitlines()) == 3
