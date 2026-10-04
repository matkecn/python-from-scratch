"""Tests for Class-creation."""

from lesson_235_class_creation import Dog


def test_barks() -> None:
    """The promise of lesson 'Class-creation' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class-creation' still holds."""
    assert Dog("Rex").name == "Rex"
