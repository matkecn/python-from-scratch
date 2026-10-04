"""Global-variables.

A variable is a name that remembers a value.

Run me:
    python 136-global-variables/lesson_136_global_variables.py
"""

from __future__ import annotations


def make_greeting(name: str) -> str:
    """Build a greeting for someone.

    Args:
        name: The person's name.

    Returns:
        A greeting that ends with an exclamation mark.

    Examples:
        >>> make_greeting("Ada")
        'Hello, Ada!'
    """
    return f"Hello, {name}!"


def swap(first: int, second: int) -> tuple[int, int]:
    """Return two numbers in the opposite order.

    Args:
        first: The number that should end up second.
        second: The number that should end up first.

    Returns:
        The two numbers, swapped.

    Examples:
        >>> swap(1, 2)
        (2, 1)
    """
    return second, first


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(make_greeting("Ada"))
    print(swap(1, 2))


if __name__ == "__main__":
    main()
