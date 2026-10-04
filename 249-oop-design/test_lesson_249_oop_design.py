"""Tests for Oop-design."""

from lesson_249_oop_design import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Oop-design' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Oop-design' still holds."""
    assert len(outline().splitlines()) == 3
