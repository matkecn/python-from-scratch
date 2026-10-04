"""Tests for Control-flow."""

from lesson_060_control_flow import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Control-flow' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Control-flow' still holds."""
    assert len(outline().splitlines()) == 3
