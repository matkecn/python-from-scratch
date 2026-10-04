"""Classes.

A class is a blueprint for making objects.

Run me:
    python 201-classes/lesson_201_classes.py
"""

from __future__ import annotations


class Dog:
    """A simple dog that can bark."""

    def __init__(self, name: str) -> None:
        """Give the dog a name.

        Args:
            name: The dog's name.
        """
        self.name = name

    def bark(self) -> str:
        """Return what the dog says.

        Returns:
            A bark that uses the dog's name.
        """
        return f"{self.name} says woof"


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    dog = Dog("Rex")
    print(dog.bark())


if __name__ == "__main__":
    main()
