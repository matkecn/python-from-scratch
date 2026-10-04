"""Tests for Class-patterns."""

from lesson_394_class_patterns import Dog


def test_barks() -> None:
    """The promise of lesson 'Class-patterns' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Class-patterns' still holds."""
    assert Dog("Rex").name == "Rex"
