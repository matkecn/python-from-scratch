"""Tests for Refactoring-challenges."""

from lesson_987_refactoring_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Refactoring-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Refactoring-challenges' still holds."""
    assert len(outline().splitlines()) == 3
