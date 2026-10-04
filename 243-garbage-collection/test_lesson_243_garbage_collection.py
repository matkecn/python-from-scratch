"""Tests for Garbage-collection."""

from lesson_243_garbage_collection import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Garbage-collection' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Garbage-collection' still holds."""
    assert len(outline().splitlines()) == 3
