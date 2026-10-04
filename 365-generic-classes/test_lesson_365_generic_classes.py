"""Tests for Generic-classes."""

from lesson_365_generic_classes import Dog


def test_barks() -> None:
    """The promise of lesson 'Generic-classes' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Generic-classes' still holds."""
    assert Dog("Rex").name == "Rex"
