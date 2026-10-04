"""Tests for Class-methods."""

from lesson_207_class_methods import Dog


def test_barks() -> None:
    """The promise of lesson 'Class-methods' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class-methods' still holds."""
    assert Dog("Rex").name == "Rex"
