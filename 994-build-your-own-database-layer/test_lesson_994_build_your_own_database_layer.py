"""Tests for Build-your-own-database-layer."""

from lesson_994_build_your_own_database_layer import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-database-layer' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-database-layer' still holds."""
    assert len(outline().splitlines()) == 3
