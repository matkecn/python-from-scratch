"""Tests for Pip-install."""

from lesson_744_pip_install import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pip-install' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pip-install' still holds."""
    assert len(outline().splitlines()) == 3
