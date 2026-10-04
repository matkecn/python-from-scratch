"""Tests for Object-references."""

from lesson_852_object_references import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Object-references' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Object-references' still holds."""
    assert len(outline().splitlines()) == 3
