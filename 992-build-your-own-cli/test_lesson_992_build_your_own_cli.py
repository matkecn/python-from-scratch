"""Tests for Build-your-own-cli."""

from lesson_992_build_your_own_cli import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-cli' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-cli' still holds."""
    assert len(outline().splitlines()) == 3
