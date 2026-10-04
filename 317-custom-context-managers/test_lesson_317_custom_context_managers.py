"""Tests for Custom-context-managers."""

from lesson_317_custom_context_managers import announce


def test_has_enter() -> None:
    """The promise of lesson 'Custom-context-managers' still holds."""
    assert hasattr(announce("x"), "__enter__")


def test_has_exit() -> None:
    """The promise of lesson 'Custom-context-managers' still holds."""
    assert hasattr(announce("x"), "__exit__")
