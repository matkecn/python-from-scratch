"""Tests for Pytest-markers."""

from lesson_724_pytest_markers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pytest-markers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pytest-markers' still holds."""
    assert len(outline().splitlines()) == 3
