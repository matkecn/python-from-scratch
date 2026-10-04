"""Tests for Scope-practice."""

from lesson_160_scope_practice import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Scope-practice' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Scope-practice' still holds."""
    assert len(outline().splitlines()) == 3
