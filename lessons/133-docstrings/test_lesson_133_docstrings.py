"""Tests for Docstrings."""

from lesson_133_docstrings import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Docstrings' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Docstrings' still holds."""
    assert len(outline().splitlines()) == 3
