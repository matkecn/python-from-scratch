"""Tests for Standard-library-project."""

from lesson_579_standard_library_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Standard-library-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Standard-library-project' still holds."""
    assert len(outline().splitlines()) == 3
