"""Tests for Stack-traces."""

from lesson_197_stack_traces import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Stack-traces' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Stack-traces' still holds."""
    assert len(outline().splitlines()) == 3
