"""Tests for Recursion-challenges."""

from lesson_971_recursion_challenges import factorial, total_length


def test_factorial_of_five() -> None:
    """The promise of lesson 'Recursion-challenges' still holds."""
    assert factorial(5) == 120


def test_zero_is_one() -> None:
    """The promise of lesson 'Recursion-challenges' still holds."""
    assert factorial(0) == 1


def test_counts_characters() -> None:
    """The promise of lesson 'Recursion-challenges' still holds."""
    assert total_length("hello") == 5
