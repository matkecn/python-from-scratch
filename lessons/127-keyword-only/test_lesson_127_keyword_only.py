"""Tests for Keyword-only."""

from lesson_127_keyword_only import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Keyword-only' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Keyword-only' still holds."""
    assert len(outline().splitlines()) == 3
