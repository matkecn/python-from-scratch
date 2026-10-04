"""Tests for Path-joining."""

from lesson_468_path_joining import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Path-joining' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Path-joining' still holds."""
    assert len(outline().splitlines()) == 3
