"""Tests for Sdist."""

from lesson_756_sdist import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sdist' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sdist' still holds."""
    assert len(outline().splitlines()) == 3
