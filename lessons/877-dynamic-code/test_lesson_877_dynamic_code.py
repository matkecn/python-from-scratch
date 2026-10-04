"""Tests for Dynamic-code."""

from lesson_877_dynamic_code import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dynamic-code' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dynamic-code' still holds."""
    assert len(outline().splitlines()) == 3
