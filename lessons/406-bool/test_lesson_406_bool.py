"""Tests for Bool."""

from lesson_406_bool import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Bool' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Bool' still holds."""
    assert len(outline().splitlines()) == 3
