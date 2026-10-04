"""Tests for Shared-memory."""

from lesson_818_shared_memory import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Shared-memory' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Shared-memory' still holds."""
    assert len(outline().splitlines()) == 3
