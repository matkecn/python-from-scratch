"""Tests for Module-search."""

from lesson_165_module_search import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Module-search' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Module-search' still holds."""
    assert len(outline().splitlines()) == 3
