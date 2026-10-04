"""Tests for Pip-freeze."""

from lesson_746_pip_freeze import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pip-freeze' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pip-freeze' still holds."""
    assert len(outline().splitlines()) == 3
