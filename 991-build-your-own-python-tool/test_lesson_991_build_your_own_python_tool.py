"""Tests for Build-your-own-python-tool."""

from lesson_991_build_your_own_python_tool import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-python-tool' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-python-tool' still holds."""
    assert len(outline().splitlines()) == 3
