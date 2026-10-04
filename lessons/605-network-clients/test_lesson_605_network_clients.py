"""Tests for Network-clients."""

from lesson_605_network_clients import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Network-clients' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Network-clients' still holds."""
    assert len(outline().splitlines()) == 3
