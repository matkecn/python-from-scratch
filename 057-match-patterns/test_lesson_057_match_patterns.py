"""Tests for Match-patterns."""

from lesson_057_match_patterns import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Match-patterns' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Match-patterns' still holds."""
    assert len(outline().splitlines()) == 3
