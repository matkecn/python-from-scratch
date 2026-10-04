"""Tests for Dynamic-classes."""

from lesson_341_dynamic_classes import Dog


def test_barks() -> None:
    """The promise of lesson 'Dynamic-classes' still holds."""
    assert Dog("Rex").bark() == "Rex says woof"


def test_keeps_the_name() -> None:
    """The promise of lesson 'Dynamic-classes' still holds."""
    assert Dog("Rex").name == "Rex"
