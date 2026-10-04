"""Tests for Metaclass-basics."""

from lesson_234_metaclass_basics import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Metaclass-basics' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Metaclass-basics' still holds."""
    assert len(outline().splitlines()) == 3
