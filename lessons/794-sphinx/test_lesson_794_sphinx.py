"""Tests for Sphinx."""

from lesson_794_sphinx import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sphinx' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sphinx' still holds."""
    assert len(outline().splitlines()) == 3
