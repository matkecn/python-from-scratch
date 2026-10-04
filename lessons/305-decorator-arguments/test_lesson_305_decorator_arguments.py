"""Tests for Decorator-arguments."""

from lesson_305_decorator_arguments import shouty, welcome


def test_shouts_result() -> None:
    """The promise of lesson 'Decorator-arguments' still holds."""
    assert welcome("Ada") == "WELCOME ADA"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Decorator-arguments' still holds."""
    assert welcome.__name__ == "welcome"
