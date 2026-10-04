"""Tests for Eval."""

from lesson_876_eval import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Eval' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Eval' still holds."""
    assert len(outline().splitlines()) == 3
