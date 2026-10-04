"""Tests for Nested-loops."""

from lesson_067_nested_loops import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Nested-loops' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Nested-loops' still holds."""
    assert len(outline().splitlines()) == 3
