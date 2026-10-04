"""Tests for Functools-wraps."""

from lesson_307_functools_wraps import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Functools-wraps' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Functools-wraps' still holds."""
    assert len(outline().splitlines()) == 3
