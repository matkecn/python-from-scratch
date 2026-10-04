"""Tests for Float-conversion."""

from lesson_033_float_conversion import average

import pytest


def test_averages() -> None:
    """The promise of lesson 'Float-conversion' still holds."""
    assert average([1.0, 2.0, 4.0]) == 2.33


def test_single_number() -> None:
    """The promise of lesson 'Float-conversion' still holds."""
    assert average([5.0]) == 5.0


def test_empty_list() -> None:
    """The promise of lesson 'Float-conversion' still holds."""
    with pytest.raises(ValueError):
        average([])
