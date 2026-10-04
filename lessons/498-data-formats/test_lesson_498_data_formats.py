"""Tests for Data-formats."""

from lesson_498_data_formats import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-formats' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-formats' still holds."""
    assert len(outline().splitlines()) == 3
