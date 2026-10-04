"""Naming.

Names are the cheapest documentation in programming. `total_price` tells you
more than `tp`.

Run me:
    python 014-naming/lesson_014_naming.py
"""

from __future__ import annotations

import keyword

TAX_RATE = 0.2


def to_snake_case(text: str) -> str:
    """Turn words into a snake_case name.

    Args:
        text: Words separated by spaces, dashes or capitals.

    Returns:
        A name using only lowercase letters, digits and underscores.

    Examples:
        >>> to_snake_case("Total Price")
        'total_price'
        >>> to_snake_case("total-price")
        'total_price'
    """
    cleaned = "".join(character.lower() if character.isalnum() else "_" for character in text)
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_")


def is_valid_name(name: str) -> bool:
    """Say whether a name is safe to use.

    Args:
        name: The name to check.

    Returns:
        ``True`` when the name starts with a letter, holds only letters,
        digits and underscores, and is not a Python keyword.

    Examples:
        >>> is_valid_name("total_price")
        True
        >>> is_valid_name("2fast")
        False
        >>> is_valid_name("class")
        False
    """
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return not name.startswith("_")


def hides_a_builtin(name: str) -> bool:
    """Say whether a name would hide something Python already has.

    Args:
        name: The name to check.

    Returns:
        ``True`` for names such as ``list`` or ``id``.

    Examples:
        >>> hides_a_builtin("list")
        True
        >>> hides_a_builtin("total_price")
        False
    """
    import builtins

    return hasattr(builtins, name)


def total_price(cost: float, quantity: int) -> float:
    """Return a price with tax added.

    Args:
        cost: The price of one item.
        quantity: How many items.

    Returns:
        The full price, rounded to two decimals.
    """
    return round(cost * quantity * (1 + TAX_RATE), 2)


def main() -> None:
    """Look at some names."""
    print(to_snake_case("Total Price"))
    print(f"total_price is a fine name: {is_valid_name('total_price')}")
    print(f"'list' hides a builtin: {hides_a_builtin('list')}")
    print(total_price(10.0, 2))


if __name__ == "__main__":
    main()
