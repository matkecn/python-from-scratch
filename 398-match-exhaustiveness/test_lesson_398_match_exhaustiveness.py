"""Tests for Match-exhaustiveness."""

from lesson_398_match_exhaustiveness import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Match-exhaustiveness' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Match-exhaustiveness' still holds."""
    assert len(outline().splitlines()) == 3
