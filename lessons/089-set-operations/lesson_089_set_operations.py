"""Set-operations.

A set keeps unique values with no duplicates.

Run me:
    python 089-set-operations/lesson_089_set_operations.py
"""

from __future__ import annotations


def unique_letters(text: str) -> set[str]:
    """Return every different letter in the text.

    Args:
        text: The text to look at.

    Returns:
        A set of letters.

    Examples:
        >>> sorted(unique_letters("aab"))
        ['a', 'b']
    """
    return set(text)


def shared(first: set[str], second: set[str]) -> set[str]:
    """Return the letters that appear in both sets.

    Args:
        first: The first set.
        second: The second set.

    Returns:
        The letters found in both.
    """
    return first & second


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(sorted(unique_letters("banana")))
    print(sorted(shared({"a", "b"}, {"b", "c"})))


if __name__ == "__main__":
    main()
