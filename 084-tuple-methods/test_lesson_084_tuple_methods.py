"""Tests for Tuple-methods."""

from lesson_084_tuple_methods import first_and_last, swap

import pytest


def test_finds_ends() -> None:
    """The promise of lesson 'Tuple-methods' still holds."""
    assert first_and_last((3, 4, 5)) == (3, 5)


def test_swaps() -> None:
    """The promise of lesson 'Tuple-methods' still holds."""
    assert swap((1, 2)) == (2, 1)


def test_empty_tuple() -> None:
    """The promise of lesson 'Tuple-methods' still holds."""
    with pytest.raises(ValueError):
        first_and_last(())
