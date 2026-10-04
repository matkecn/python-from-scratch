"""Tests for Pyproject."""

from lesson_751_pyproject import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pyproject' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pyproject' still holds."""
    assert len(outline().splitlines()) == 3
