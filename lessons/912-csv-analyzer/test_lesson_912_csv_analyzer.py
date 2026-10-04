"""Tests for Csv-analyzer."""

from lesson_912_csv_analyzer import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Csv-analyzer' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Csv-analyzer' still holds."""
    assert len(outline().splitlines()) == 3
