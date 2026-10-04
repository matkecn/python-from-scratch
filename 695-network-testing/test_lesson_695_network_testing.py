"""Tests for Network-testing."""

from lesson_695_network_testing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Network-testing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Network-testing' still holds."""
    assert len(outline().splitlines()) == 3
