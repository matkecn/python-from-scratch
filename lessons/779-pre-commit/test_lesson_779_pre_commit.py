"""Tests for Pre-commit."""

from lesson_779_pre_commit import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pre-commit' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pre-commit' still holds."""
    assert len(outline().splitlines()) == 3
