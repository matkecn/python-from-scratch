"""Tests for Watch-expressions."""

from lesson_705_watch_expressions import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Watch-expressions' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Watch-expressions' still holds."""
    assert len(outline().splitlines()) == 3
