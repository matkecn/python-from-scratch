"""Tests for Data-descriptors."""

from lesson_330_data_descriptors import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Data-descriptors' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Data-descriptors' still holds."""
    assert len(outline().splitlines()) == 3
