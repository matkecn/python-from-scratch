"""Tests for Sub."""

from lesson_417_sub import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sub' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sub' still holds."""
    assert len(outline().splitlines()) == 3
