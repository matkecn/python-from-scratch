"""Tests for Rsub."""

from lesson_427_rsub import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Rsub' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Rsub' still holds."""
    assert len(outline().splitlines()) == 3
