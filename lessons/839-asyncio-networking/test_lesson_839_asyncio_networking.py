"""Tests for Asyncio-networking."""

from lesson_839_asyncio_networking import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Asyncio-networking' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Asyncio-networking' still holds."""
    assert len(outline().splitlines()) == 3
