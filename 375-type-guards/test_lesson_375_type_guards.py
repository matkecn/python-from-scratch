"""Tests for Type-guards."""

from lesson_375_type_guards import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-guards' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-guards' still holds."""
    assert len(outline().splitlines()) == 3
