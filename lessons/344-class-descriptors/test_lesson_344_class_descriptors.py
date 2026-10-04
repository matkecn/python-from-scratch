"""Tests for Class-descriptors."""

from lesson_344_class_descriptors import Dog


def test_barks() -> None:
    """The promise of lesson 'Class-descriptors' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class-descriptors' still holds."""
    assert Dog("Rex").name == "Rex"
