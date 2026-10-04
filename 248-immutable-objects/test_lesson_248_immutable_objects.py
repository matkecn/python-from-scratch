"""Tests for Immutable-objects."""

from lesson_248_immutable_objects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Immutable-objects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Immutable-objects' still holds."""
    assert len(outline().splitlines()) == 3
