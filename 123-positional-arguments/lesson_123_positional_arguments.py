"""Positional-arguments.

Arguments are the values you hand to a function.

Run me:
    python 123-positional-arguments/lesson_123_positional_arguments.py
"""

from __future__ import annotations


def greet(name: str, greeting: str = "Hello") -> str:
    """Build a greeting.

    Args:
        name: Who to greet.
        greeting: The word to use first.

    Returns:
        The full greeting.

    Examples:
        >>> greet("Ada")
        'Hello, Ada'
        >>> greet("Ada", greeting="Hi")
        'Hi, Ada'
    """
    return f"{greeting}, {name}"


def total_price(cost: float, quantity: int, *, tax: float = 0.0) -> float:
    """Work out a price with tax.

    Args:
        cost: The price of one item.
        quantity: How many items.
        tax: The tax rate, so ``0.2`` means twenty percent.

    Returns:
        The full price, rounded to two decimals.
    """
    return round(cost * quantity * (1 + tax), 2)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(greet("Ada"))
    print(total_price(2.5, 3, tax=0.2))


if __name__ == "__main__":
    main()
