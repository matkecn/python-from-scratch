"""Tests for Packaging-challenges."""

from lesson_989_packaging_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Packaging-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Packaging-challenges' still holds."""
    assert len(outline().splitlines()) == 3
