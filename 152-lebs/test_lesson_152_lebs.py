"""Tests for Scope labs."""

from lesson_152_lebs import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Scope labs' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Scope labs' still holds."""
    assert len(outline().splitlines()) == 3
