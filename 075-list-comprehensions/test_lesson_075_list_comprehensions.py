"""Tests for List-comprehensions."""

from lesson_075_list_comprehensions import add_up, biggest

import pytest


def test_sums() -> None:
    """The promise of lesson 'List-comprehensions' still holds."""
    assert add_up([1, 2, 3]) == 6


def test_finds_biggest() -> None:
    """The promise of lesson 'List-comprehensions' still holds."""
    assert biggest([4, 9, 2]) == 9


def test_empty_list() -> None:
    """The promise of lesson 'List-comprehensions' still holds."""
    with pytest.raises(ValueError):
        biggest([])
