"""Tests for Sorted."""

from lesson_145_sorted import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sorted' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sorted' still holds."""
    assert len(outline().splitlines()) == 3
