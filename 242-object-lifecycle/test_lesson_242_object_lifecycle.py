"""Tests for Object-lifecycle."""

from lesson_242_object_lifecycle import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Object-lifecycle' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Object-lifecycle' still holds."""
    assert len(outline().splitlines()) == 3
