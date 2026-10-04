"""Tests for Throw."""

from lesson_263_throw import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Throw' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Throw' still holds."""
    assert len(outline().splitlines()) == 3
