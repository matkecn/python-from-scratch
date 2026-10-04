"""Tests for Csv-dialects."""

from lesson_489_csv_dialects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Csv-dialects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Csv-dialects' still holds."""
    assert len(outline().splitlines()) == 3
