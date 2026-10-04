"""Tests for Type-checkers."""

from lesson_371_type_checkers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-checkers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-checkers' still holds."""
    assert len(outline().splitlines()) == 3
