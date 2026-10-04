"""Tests for Async-context-manager."""

from lesson_440_async_context_manager import announce


def test_has_enter() -> None:
    """The promise of lesson 'Async-context-manager' still holds."""
    assert hasattr(announce("x"), "__enter__")


def test_has_exit() -> None:
    """The promise of lesson 'Async-context-manager' still holds."""
    assert hasattr(announce("x"), "__exit__")
