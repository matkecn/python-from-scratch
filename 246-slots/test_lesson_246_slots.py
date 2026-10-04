"""Tests for Slots."""

from lesson_246_slots import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Slots' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Slots' still holds."""
    assert len(outline().splitlines()) == 3
