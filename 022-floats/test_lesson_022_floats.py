"""Tests for Floats."""

from lesson_022_floats import average

import pytest


def test_averages() -> None:
    """The promise of lesson 'Floats' still holds."""
    assert average([1.0, 2.0, 4.0]) == 2.33


def test_single_number() -> None:
    """The promise of lesson 'Floats' still holds."""
    assert average([5.0]) == 5.0


def test_empty_list() -> None:
    """The promise of lesson 'Floats' still holds."""
    with pytest.raises(ValueError):
        average([])
