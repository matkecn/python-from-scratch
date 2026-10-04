"""Tests for Pytest-plugins."""

from lesson_726_pytest_plugins import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pytest-plugins' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pytest-plugins' still holds."""
    assert len(outline().splitlines()) == 3
