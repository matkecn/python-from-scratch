"""Tests for Path-objects."""

from lesson_467_path_objects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Path-objects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Path-objects' still holds."""
    assert len(outline().splitlines()) == 3
