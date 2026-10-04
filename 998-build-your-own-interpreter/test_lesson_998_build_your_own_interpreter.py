"""Tests for Build-your-own-interpreter."""

from lesson_998_build_your_own_interpreter import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-interpreter' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-interpreter' still holds."""
    assert len(outline().splitlines()) == 3
