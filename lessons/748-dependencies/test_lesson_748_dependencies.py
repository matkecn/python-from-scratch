"""Tests for Dependencies."""

from lesson_748_dependencies import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dependencies' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dependencies' still holds."""
    assert len(outline().splitlines()) == 3
