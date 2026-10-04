"""Tests for Decorator-factories."""

from lesson_304_decorator_factories import shouty, welcome


def test_shouts_result() -> None:
    """The promise of lesson 'Decorator-factories' still holds."""
    assert welcome("Ada") == "WELCOME ADA"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Decorator-factories' still holds."""
    assert welcome.__name__ == "welcome"
