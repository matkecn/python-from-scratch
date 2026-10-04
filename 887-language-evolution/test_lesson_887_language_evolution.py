"""Tests for Language-evolution."""

from lesson_887_language_evolution import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Language-evolution' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Language-evolution' still holds."""
    assert len(outline().splitlines()) == 3
