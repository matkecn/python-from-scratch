"""Tests for Pip-tools."""

from lesson_763_pip_tools import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pip-tools' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pip-tools' still holds."""
    assert len(outline().splitlines()) == 3
