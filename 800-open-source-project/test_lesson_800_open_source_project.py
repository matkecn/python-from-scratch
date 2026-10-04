"""Tests for Open-source-project."""

from lesson_800_open_source_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Open-source-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Open-source-project' still holds."""
    assert len(outline().splitlines()) == 3
