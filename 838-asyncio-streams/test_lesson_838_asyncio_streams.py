"""Tests for Asyncio-streams."""

from lesson_838_asyncio_streams import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Asyncio-streams' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Asyncio-streams' still holds."""
    assert len(outline().splitlines()) == 3
