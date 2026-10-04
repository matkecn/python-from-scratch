"""Tests for Matrix basics."""

from lesson_519_matrix_basics import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Matrix basics' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Matrix basics' still holds."""
    assert len(outline().splitlines()) == 3
