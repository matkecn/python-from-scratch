"""Tests for Kwargs."""

from lesson_129_kwargs import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Kwargs' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Kwargs' still holds."""
    assert len(outline().splitlines()) == 3
