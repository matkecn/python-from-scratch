"""Tests for Decorators."""

from lesson_301_decorators import shouty, welcome


def test_shouts_result() -> None:
    """The promise of lesson 'Decorators' still holds."""
    assert welcome("Ada") == "WELCOME ADA"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Decorators' still holds."""
    assert welcome.__name__ == "welcome"
