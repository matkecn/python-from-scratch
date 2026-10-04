"""Tests for Lazy-evaluation."""

from lesson_267_lazy_evaluation import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Lazy-evaluation' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Lazy-evaluation' still holds."""
    assert len(outline().splitlines()) == 3
