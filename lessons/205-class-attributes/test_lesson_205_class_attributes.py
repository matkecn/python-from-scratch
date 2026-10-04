"""Tests for Class-attributes."""

from lesson_205_class_attributes import Dog


def test_barks() -> None:
    """The promise of lesson 'Class-attributes' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class-attributes' still holds."""
    assert Dog("Rex").name == "Rex"
