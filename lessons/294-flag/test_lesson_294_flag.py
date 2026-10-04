"""Tests for Flag."""

from lesson_294_flag import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Flag' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Flag' still holds."""
    assert len(outline().splitlines()) == 3
