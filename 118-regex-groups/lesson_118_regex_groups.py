"""Regex-groups.

Regular expressions find patterns inside text.

Run me:
    python 118-regex-groups/lesson_118_regex_groups.py
"""

from __future__ import annotations


import re


def find_digits(text: str) -> list[str]:
    """Return every run of digits in the text.

    Args:
        text: The text to search.

    Returns:
        The digit groups, in order.

    Examples:
        >>> find_digits("a1 b22")
        ['1', '22']
    """
    return re.findall(r"\d+", text)


def is_valid_pin(pin: str) -> bool:
    """Say whether a pin is exactly four digits.

    Args:
        pin: The pin to check.

    Returns:
        ``True`` when the pin is four digits.

    Examples:
        >>> is_valid_pin("1234")
        True
    """
    return bool(re.fullmatch(r"\d{4}", pin))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(find_digits("a1 b22"))
    print(is_valid_pin("1234"), is_valid_pin("12"))


if __name__ == "__main__":
    main()
