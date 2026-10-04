"""Tests for argparse."""

from lesson_581_argparse import build_parser, greeting_for


def test_greets_twice() -> None:
    """The promise of lesson 'argparse' still holds."""
    assert greeting_for("Ada", 2) == "Hello, Ada!\nHello, Ada!"


def test_greets_once() -> None:
    """The promise of lesson 'argparse' still holds."""
    assert greeting_for("Ada", 1) == "Hello, Ada!"
