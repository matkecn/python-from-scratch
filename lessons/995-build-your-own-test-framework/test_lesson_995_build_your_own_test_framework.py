"""Tests for Build-your-own-test-framework."""

from lesson_995_build_your_own_test_framework import add


def test_adds_small_numbers() -> None:
    """The promise of lesson 'Build-your-own-test-framework' still holds."""
    assert add(2, 3) == 5


def test_adds_zero() -> None:
    """The promise of lesson 'Build-your-own-test-framework' still holds."""
    assert add(0, 0) == 0
