"""Tests for Itertools-islice."""

from lesson_278_itertools_islice import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-islice' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-islice' still holds."""
    assert len(outline().splitlines()) == 3
