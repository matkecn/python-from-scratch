"""Dictionary-indexing.

A dictionary stores values under keys, like a phone book.

Run me:
    python 092-dictionary-indexing/lesson_092_dictionary_indexing.py
"""

from __future__ import annotations


def word_lengths(text: str) -> dict[str, int]:
    """Map each word to the number of letters it has.

    Args:
        text: A sentence.

    Returns:
        A dictionary of word to length.

    Examples:
        >>> word_lengths("a bb")
        {'a': 1, 'bb': 2}
    """
    return {word: len(word) for word in text.split()}


def lookup(ages: dict[str, int], name: str) -> int:
    """Return someone's age, or ``-1`` when we do not know them.

    Args:
        ages: A mapping of name to age.
        name: The person to look up.

    Returns:
        The age, or ``-1``.

    Examples:
        >>> lookup({"Ada": 36}, "Bo")
        -1
    """
    return ages.get(name, -1)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(word_lengths("a bb ccc"))
    print(lookup({"Ada": 36}, "Bo"))


if __name__ == "__main__":
    main()
