"""Tests for If."""

from lesson_051_if import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'If' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'If' still holds."""
    assert len(outline().splitlines()) == 3
