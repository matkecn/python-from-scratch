"""Tests for Star-unpacking."""

from lesson_080_star_unpacking import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Star-unpacking' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Star-unpacking' still holds."""
    assert len(outline().splitlines()) == 3
