"""Tests for Batch-renamer."""

from lesson_918_batch_renamer import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Batch-renamer' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Batch-renamer' still holds."""
    assert len(outline().splitlines()) == 3
