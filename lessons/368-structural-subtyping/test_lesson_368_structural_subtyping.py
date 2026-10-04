"""Tests for Structural-subtyping."""

from lesson_368_structural_subtyping import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Structural-subtyping' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Structural-subtyping' still holds."""
    assert len(outline().splitlines()) == 3
