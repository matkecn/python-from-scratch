"""Tests for Frozen-dataclasses."""

from lesson_385_frozen_dataclasses import Point

import pytest


def test_keeps_values() -> None:
    """The promise of lesson 'Frozen-dataclasses' still holds."""
    assert Point(3, 4).x == 3


def test_measures_distance() -> None:
    """The promise of lesson 'Frozen-dataclasses' still holds."""
    assert Point(3, 4).distance_from_origin() == 5.0


def test_cannot_change() -> None:
    """The promise of lesson 'Frozen-dataclasses' still holds."""
    with pytest.raises(Exception):
        setattr(Point(1, 1), 'x', 2)
