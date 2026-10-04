"""Tests for Directory-statistics."""

from lesson_919_directory_statistics import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Directory-statistics' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Directory-statistics' still holds."""
    assert len(outline().splitlines()) == 3
