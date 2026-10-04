"""Tests for Text-processing-project."""

from lesson_578_text_processing_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Text-processing-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Text-processing-project' still holds."""
    assert len(outline().splitlines()) == 3
