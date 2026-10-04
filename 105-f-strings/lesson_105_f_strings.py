"""F-strings.

F-strings let you drop values straight into text.

Run me:
    python 105-f-strings/lesson_105_f_strings.py
"""

from __future__ import annotations


def price_line(item: str, price: float) -> str:
    """Return one line of a receipt.

    Args:
        item: The name of the item.
        price: The price of one item.

    Returns:
        A line such as ``"Tea: 2.50"``.

    Examples:
        >>> price_line("Tea", 2.5)
        'Tea: 2.50'
    """
    return f"{item}: {price:.2f}"


def progress(done: int, total: int) -> str:
    """Return a tiny progress bar.

    Args:
        done: How many steps are finished.
        total: How many steps there are.

    Returns:
        A bar such as ``"[##----]"``.

    Examples:
        >>> progress(2, 6)
        '[##----]'
    """
    filled = round(done / total * 6)
    return "[" + "#" * filled + "-" * (6 - filled) + "]"


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(price_line("Tea", 2.5))
    print(progress(2, 6))


if __name__ == "__main__":
    main()
