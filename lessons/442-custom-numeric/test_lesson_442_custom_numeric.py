"""Tests for Custom-numeric."""

from lesson_442_custom_numeric import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Custom-numeric' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Custom-numeric' still holds."""
    assert len(outline().splitlines()) == 3
