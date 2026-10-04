"""Tests for Packaging-capstone."""

from lesson_770_packaging_capstone import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Packaging-capstone' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Packaging-capstone' still holds."""
    assert len(outline().splitlines()) == 3
