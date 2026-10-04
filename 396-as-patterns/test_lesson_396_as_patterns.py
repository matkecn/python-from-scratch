"""Tests for As-patterns."""

from lesson_396_as_patterns import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'As-patterns' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'As-patterns' still holds."""
    assert len(outline().splitlines()) == 3
