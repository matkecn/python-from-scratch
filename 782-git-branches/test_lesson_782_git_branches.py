"""Tests for Git-branches."""

from lesson_782_git_branches import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Git-branches' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Git-branches' still holds."""
    assert len(outline().splitlines()) == 3
