"""Tests for Method-descriptors."""

from lesson_328_method_descriptors import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Method-descriptors' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Method-descriptors' still holds."""
    assert len(outline().splitlines()) == 3
