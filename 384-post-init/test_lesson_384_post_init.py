"""Tests for Post-init."""

from lesson_384_post_init import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Post-init' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Post-init' still holds."""
    assert len(outline().splitlines()) == 3
