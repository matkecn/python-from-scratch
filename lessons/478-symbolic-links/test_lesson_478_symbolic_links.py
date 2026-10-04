"""Tests for Symbolic-links."""

from lesson_478_symbolic_links import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Symbolic-links' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Symbolic-links' still holds."""
    assert len(outline().splitlines()) == 3
