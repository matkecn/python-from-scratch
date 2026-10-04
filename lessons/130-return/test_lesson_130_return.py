"""Tests for Return."""

from lesson_130_return import divide

import pytest


def test_splits_fairly() -> None:
    """The promise of lesson 'Return' still holds."""
    assert divide(8, 3) == (2, 2)


def test_no_left_over() -> None:
    """The promise of lesson 'Return' still holds."""
    assert divide(9, 3) == (3, 0)


def test_no_people() -> None:
    """The promise of lesson 'Return' still holds."""
    with pytest.raises(ValueError):
        divide(8, 0)
