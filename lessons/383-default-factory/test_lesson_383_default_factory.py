"""Tests for Default-factory."""

from lesson_383_default_factory import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Default-factory' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Default-factory' still holds."""
    assert len(outline().splitlines()) == 3
