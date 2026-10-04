"""Tests for Data-structure-challenges."""

from lesson_967_data_structure_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-structure-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-structure-challenges' still holds."""
    assert len(outline().splitlines()) == 3
