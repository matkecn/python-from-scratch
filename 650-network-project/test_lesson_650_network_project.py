"""Tests for Network-project."""

from lesson_650_network_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Network-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Network-project' still holds."""
    assert len(outline().splitlines()) == 3
