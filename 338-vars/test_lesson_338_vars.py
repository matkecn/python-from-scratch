"""Tests for Vars."""

from lesson_338_vars import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Vars' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Vars' still holds."""
    assert len(outline().splitlines()) == 3
