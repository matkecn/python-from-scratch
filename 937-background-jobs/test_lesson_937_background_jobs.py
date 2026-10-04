"""Tests for Background-jobs."""

from lesson_937_background_jobs import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Background-jobs' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Background-jobs' still holds."""
    assert len(outline().splitlines()) == 3
