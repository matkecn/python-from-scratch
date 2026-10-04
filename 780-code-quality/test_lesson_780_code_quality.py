"""Tests for Code-quality."""

from lesson_780_code_quality import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Code-quality' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Code-quality' still holds."""
    assert len(outline().splitlines()) == 3
