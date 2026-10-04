"""Tests for Type-narrowing."""

from lesson_374_type_narrowing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-narrowing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-narrowing' still holds."""
    assert len(outline().splitlines()) == 3
