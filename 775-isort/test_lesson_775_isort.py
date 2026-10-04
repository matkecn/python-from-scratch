"""Tests for Isort."""

from lesson_775_isort import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Isort' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Isort' still holds."""
    assert len(outline().splitlines()) == 3
