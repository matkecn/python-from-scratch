"""Tests for Custom-context-manager."""

from lesson_447_custom_context_manager import announce


def test_has_enter() -> None:
    """The promise of lesson 'Custom-context-manager' still holds."""
    assert hasattr(announce("x"), "__enter__")


def test_has_exit() -> None:
    """The promise of lesson 'Custom-context-manager' still holds."""
    assert hasattr(announce("x"), "__exit__")
