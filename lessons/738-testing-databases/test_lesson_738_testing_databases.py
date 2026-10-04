"""Tests for Testing-databases."""

from lesson_738_testing_databases import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Testing-databases' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Testing-databases' still holds."""
    assert len(outline().splitlines()) == 3
