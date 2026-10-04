"""Tests for Code-coverage."""

from lesson_728_code_coverage import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Code-coverage' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Code-coverage' still holds."""
    assert len(outline().splitlines()) == 3
