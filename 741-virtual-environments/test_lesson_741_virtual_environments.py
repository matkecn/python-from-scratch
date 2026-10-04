"""Tests for Virtual-environments."""

from lesson_741_virtual_environments import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Virtual-environments' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Virtual-environments' still holds."""
    assert len(outline().splitlines()) == 3
