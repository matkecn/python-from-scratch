"""Tests for Concurrency-challenges."""

from lesson_979_concurrency_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Concurrency-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Concurrency-challenges' still holds."""
    assert len(outline().splitlines()) == 3
