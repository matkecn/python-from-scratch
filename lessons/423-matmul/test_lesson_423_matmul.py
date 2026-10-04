"""Tests for __matmul__."""

from lesson_423_matmul import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson '__matmul__' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson '__matmul__' still holds."""
    assert len(outline().splitlines()) == 3
