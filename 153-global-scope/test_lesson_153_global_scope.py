"""Tests for Global-scope."""

from lesson_153_global_scope import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Global-scope' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Global-scope' still holds."""
    assert len(outline().splitlines()) == 3
