"""Tests for Functional-challenges."""

from lesson_973_functional_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Functional-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Functional-challenges' still holds."""
    assert len(outline().splitlines()) == 3
