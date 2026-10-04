"""Tests for Pagination."""

from lesson_638_pagination import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pagination' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pagination' still holds."""
    assert len(outline().splitlines()) == 3
