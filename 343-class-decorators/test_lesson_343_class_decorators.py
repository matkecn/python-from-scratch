"""Tests for Class-decorators."""

from lesson_343_class_decorators import Dog


def test_barks() -> None:
    """The promise of lesson 'Class-decorators' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class-decorators' still holds."""
    assert Dog("Rex").name == "Rex"
