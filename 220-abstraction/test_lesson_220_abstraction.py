"""Tests for Abstraction."""

from lesson_220_abstraction import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Abstraction' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Abstraction' still holds."""
    assert len(outline().splitlines()) == 3
