"""Tests for Socket-debugging."""

from lesson_696_socket_debugging import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Socket-debugging' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Socket-debugging' still holds."""
    assert len(outline().splitlines()) == 3
