"""Tests for Classes."""

from lesson_201_classes import Dog


def test_barks() -> None:
    """The promise of lesson 'Classes' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Classes' still holds."""
    assert Dog("Rex").name == "Rex"
