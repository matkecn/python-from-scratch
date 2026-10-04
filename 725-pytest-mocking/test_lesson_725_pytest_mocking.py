"""Tests for Pytest-mocking."""

from lesson_725_pytest_mocking import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pytest-mocking' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pytest-mocking' still holds."""
    assert len(outline().splitlines()) == 3
