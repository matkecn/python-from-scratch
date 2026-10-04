"""Tests for Or-patterns."""

from lesson_395_or_patterns import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Or-patterns' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Or-patterns' still holds."""
    assert len(outline().splitlines()) == 3
