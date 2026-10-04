"""Tests for Joins."""

from lesson_636_joins import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Joins' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Joins' still holds."""
    assert len(outline().splitlines()) == 3
