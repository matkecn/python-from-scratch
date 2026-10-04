"""Tests for Keyword-arguments."""

from lesson_124_keyword_arguments import greet, total_price


def test_default_greeting() -> None:
    """The promise of lesson 'Keyword-arguments' still holds."""
    assert greet("Ada") == "Hello, Ada"


def test_keyword_greeting() -> None:
    """The promise of lesson 'Keyword-arguments' still holds."""
    assert greet("Ada", greeting="Hi") == "Hi, Ada"


def test_adds_tax() -> None:
    """The promise of lesson 'Keyword-arguments' still holds."""
    assert total_price(10.0, 2, tax=0.1) == 22.0
