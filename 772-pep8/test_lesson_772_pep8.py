"""Tests for Pep8."""

from lesson_772_pep8 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pep8' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pep8' still holds."""
    assert len(outline().splitlines()) == 3
