"""Tests for Network-debugging."""

from lesson_691_network_debugging import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Network-debugging' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Network-debugging' still holds."""
    assert len(outline().splitlines()) == 3
