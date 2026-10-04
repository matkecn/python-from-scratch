"""Tests for Client-server."""

from lesson_652_client_server import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Client-server' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Client-server' still holds."""
    assert len(outline().splitlines()) == 3
