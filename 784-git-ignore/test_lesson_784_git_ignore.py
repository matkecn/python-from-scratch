"""Tests for Git-ignore."""

from lesson_784_git_ignore import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Git-ignore' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Git-ignore' still holds."""
    assert len(outline().splitlines()) == 3
