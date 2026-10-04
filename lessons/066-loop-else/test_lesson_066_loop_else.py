"""Tests for Loop-else."""

from lesson_066_loop_else import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Loop-else' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Loop-else' still holds."""
    assert len(outline().splitlines()) == 3
