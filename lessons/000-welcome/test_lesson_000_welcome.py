"""Tests for the welcome lesson."""

from lesson_000_welcome import greet, hello_world


def test_hello_world_is_the_classic_line() -> None:
    """The first line every programmer writes still works."""
    assert hello_world() == "Hello, world!"


def test_greet_uses_the_name() -> None:
    """A name in, a greeting out."""
    assert greet("Ada") == "Hello, Ada!"


def test_greet_falls_back_to_world() -> None:
    """An empty name still gives a friendly greeting."""
    assert greet("") == "Hello, world!"
