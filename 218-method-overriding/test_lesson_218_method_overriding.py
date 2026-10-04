"""Tests for Method-overriding."""

from lesson_218_method_overriding import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Method-overriding' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Method-overriding' still holds."""
    assert len(outline().splitlines()) == 3
