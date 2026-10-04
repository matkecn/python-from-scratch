"""Tests for Data-processing-project."""

from lesson_920_data_processing_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-processing-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-processing-project' still holds."""
    assert len(outline().splitlines()) == 3
