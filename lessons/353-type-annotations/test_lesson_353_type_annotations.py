"""Tests for Type-annotations."""

from lesson_353_type_annotations import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-annotations' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-annotations' still holds."""
    assert len(outline().splitlines()) == 3
