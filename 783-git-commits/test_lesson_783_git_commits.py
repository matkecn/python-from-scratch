"""Tests for Git-commits."""

from lesson_783_git_commits import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Git-commits' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Git-commits' still holds."""
    assert len(outline().splitlines()) == 3
