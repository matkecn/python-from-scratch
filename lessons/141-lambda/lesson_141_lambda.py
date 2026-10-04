"""Lambda.

A lambda is a tiny function with no name and no body.

Run me:
    python 141-lambda/lesson_141_lambda.py
"""

from __future__ import annotations


def add_tax(price: float) -> float:
    """Add twenty percent tax to a price.

    Args:
        price: The price before tax.

    Returns:
        The price with tax.

    Examples:
        >>> add_tax(10.0)
        12.0
    """
    with_tax = lambda value: round(value * 1.2, 2)
    return with_tax(price)


def by_length(words: list[str]) -> list[str]:
    """Sort words from longest to shortest.

    Args:
        words: The words to sort.

    Returns:
        A new sorted list.
    """
    return sorted(words, key=lambda word: len(word), reverse=True)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(add_tax(10.0))
    print(by_length(["pear", "fig", "banana"]))


if __name__ == "__main__":
    main()
