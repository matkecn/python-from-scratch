"""Tests for Network-servers."""

from lesson_606_network_servers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Network-servers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Network-servers' still holds."""
    assert len(outline().splitlines()) == 3
