"""Tests for Shallow-copy."""

from lesson_241_shallow_copy import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Shallow-copy' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Shallow-copy' still holds."""
    assert len(outline().splitlines()) == 3
