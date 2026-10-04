"""Tests for Cpython-source."""

from lesson_899_cpython_source import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cpython-source' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cpython-source' still holds."""
    assert len(outline().splitlines()) == 3
