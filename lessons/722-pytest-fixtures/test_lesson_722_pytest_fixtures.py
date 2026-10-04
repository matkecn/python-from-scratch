"""Tests for Pytest-fixtures."""

from lesson_722_pytest_fixtures import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pytest-fixtures' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pytest-fixtures' still holds."""
    assert len(outline().splitlines()) == 3
