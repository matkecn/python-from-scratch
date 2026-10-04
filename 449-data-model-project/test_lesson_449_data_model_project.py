"""Tests for Data-model-project."""

from lesson_449_data_model_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-model-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-model-project' still holds."""
    assert len(outline().splitlines()) == 3
