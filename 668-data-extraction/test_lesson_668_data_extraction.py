"""Tests for Data-extraction."""

from lesson_668_data_extraction import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-extraction' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-extraction' still holds."""
    assert len(outline().splitlines()) == 3
