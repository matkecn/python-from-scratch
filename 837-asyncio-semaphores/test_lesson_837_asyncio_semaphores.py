"""Tests for Asyncio-semaphores."""

from lesson_837_asyncio_semaphores import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Asyncio-semaphores' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Asyncio-semaphores' still holds."""
    assert len(outline().splitlines()) == 3
