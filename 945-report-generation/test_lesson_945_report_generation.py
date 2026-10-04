"""Tests for Report-generation."""

from lesson_945_report_generation import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Report-generation' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Report-generation' still holds."""
    assert len(outline().splitlines()) == 3
