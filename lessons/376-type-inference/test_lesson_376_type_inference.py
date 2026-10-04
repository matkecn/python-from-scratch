"""Tests for Type-inference."""

from lesson_376_type_inference import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-inference' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-inference' still holds."""
    assert len(outline().splitlines()) == 3
