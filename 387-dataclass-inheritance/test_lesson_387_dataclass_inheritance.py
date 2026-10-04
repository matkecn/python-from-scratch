"""Tests for Dataclass-inheritance."""

from lesson_387_dataclass_inheritance import Point

import pytest


def test_keeps_values() -> None:
    """The promise of lesson 'Dataclass-inheritance' still holds."""
    assert Point(3, 4).x == 3


def test_measures_distance() -> None:
    """The promise of lesson 'Dataclass-inheritance' still holds."""
    assert Point(3, 4).distance_from_origin() == 5.0


def test_cannot_change() -> None:
    """The promise of lesson 'Dataclass-inheritance' still holds."""
    with pytest.raises(Exception):
        setattr(Point(1, 1), 'x', 2)
