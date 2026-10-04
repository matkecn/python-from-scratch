"""Tests for Garbage-collection-internals."""

from lesson_894_garbage_collection_internals import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Garbage-collection-internals' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Garbage-collection-internals' still holds."""
    assert len(outline().splitlines()) == 3
