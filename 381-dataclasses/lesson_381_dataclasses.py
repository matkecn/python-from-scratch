"""Dataclasses.

A dataclass writes the boring parts of a class for you.

Run me:
    python 381-dataclasses/lesson_381_dataclasses.py
"""

from __future__ import annotations


from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """A point on a grid."""

    x: int
    y: int

    def distance_from_origin(self) -> float:
        """Return how far the point is from ``0, 0``.

        Returns:
            The distance, as a float.
        """
        return (self.x**2 + self.y**2) ** 0.5


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    point = Point(3, 4)
    print(point)
    print(round(point.distance_from_origin(), 2))


if __name__ == "__main__":
    main()
