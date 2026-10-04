"""Tests for While."""

from lesson_062_while import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'While' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'While' still holds."""
    assert len(outline().splitlines()) == 3
