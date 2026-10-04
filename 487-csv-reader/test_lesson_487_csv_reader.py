"""Tests for Csv-reader."""

from lesson_487_csv_reader import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Csv-reader' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Csv-reader' still holds."""
    assert len(outline().splitlines()) == 3
