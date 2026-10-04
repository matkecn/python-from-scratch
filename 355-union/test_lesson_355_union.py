"""Tests for Union."""

from lesson_355_union import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Union' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Union' still holds."""
    assert len(outline().splitlines()) == 3
