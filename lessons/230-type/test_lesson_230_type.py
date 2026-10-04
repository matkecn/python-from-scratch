"""Tests for Type."""

from lesson_230_type import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type' still holds."""
    assert len(outline().splitlines()) == 3
