"""Tests for Wheel."""

from lesson_755_wheel import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Wheel' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Wheel' still holds."""
    assert len(outline().splitlines()) == 3
