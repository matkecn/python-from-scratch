"""Tests for Garbage-collector."""

from lesson_854_garbage_collector import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Garbage-collector' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Garbage-collector' still holds."""
    assert len(outline().splitlines()) == 3
