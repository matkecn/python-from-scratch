"""Tests for Custom-sequence."""

from lesson_445_custom_sequence import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Custom-sequence' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Custom-sequence' still holds."""
    assert len(outline().splitlines()) == 3
