"""Tests for Ip-addresses."""

from lesson_604_ip_addresses import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ip-addresses' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ip-addresses' still holds."""
    assert len(outline().splitlines()) == 3
