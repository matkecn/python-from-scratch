"""Tests for Algorithm-challenges."""

from lesson_966_algorithm_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Algorithm-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Algorithm-challenges' still holds."""
    assert len(outline().splitlines()) == 3
