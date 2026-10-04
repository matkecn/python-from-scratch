"""Tests for Pytest-parametrize."""

from lesson_723_pytest_parametrize import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pytest-parametrize' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pytest-parametrize' still holds."""
    assert len(outline().splitlines()) == 3
