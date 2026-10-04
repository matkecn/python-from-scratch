"""Tests for Csv-writer."""

from lesson_488_csv_writer import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Csv-writer' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Csv-writer' still holds."""
    assert len(outline().splitlines()) == 3
