"""Tests for Sizeof."""

from lesson_408_sizeof import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sizeof' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sizeof' still holds."""
    assert len(outline().splitlines()) == 3
