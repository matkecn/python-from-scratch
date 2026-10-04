"""Tests for First-class-functions."""

from lesson_140_first_class_functions import Dog


def test_barks() -> None:
    """The promise of lesson 'First-class-functions' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'First-class-functions' still holds."""
    assert Dog("Rex").name == "Rex"
