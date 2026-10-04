"""Tests for Runtime-checkable."""

from lesson_369_runtime_checkable import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Runtime-checkable' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Runtime-checkable' still holds."""
    assert len(outline().splitlines()) == 3
