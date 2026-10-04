"""Tests for Class."""

from lesson_210_class import Dog


def test_barks() -> None:
    """The promise of lesson 'Class' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class' still holds."""
    assert Dog("Rex").name == "Rex"
