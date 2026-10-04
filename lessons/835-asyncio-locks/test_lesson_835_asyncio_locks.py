"""Tests for Asyncio-locks."""

from lesson_835_asyncio_locks import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Asyncio-locks' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Asyncio-locks' still holds."""
    assert len(outline().splitlines()) == 3
