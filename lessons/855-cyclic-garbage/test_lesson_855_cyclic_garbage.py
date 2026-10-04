"""Tests for Cyclic-garbage."""

from lesson_855_cyclic_garbage import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cyclic-garbage' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cyclic-garbage' still holds."""
    assert len(outline().splitlines()) == 3
