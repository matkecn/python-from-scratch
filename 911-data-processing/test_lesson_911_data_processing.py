"""Tests for Data-processing."""

from lesson_911_data_processing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-processing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-processing' still holds."""
    assert len(outline().splitlines()) == 3
