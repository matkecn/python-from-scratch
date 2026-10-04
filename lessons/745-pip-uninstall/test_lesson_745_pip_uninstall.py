"""Tests for Pip-uninstall."""

from lesson_745_pip_uninstall import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pip-uninstall' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pip-uninstall' still holds."""
    assert len(outline().splitlines()) == 3
