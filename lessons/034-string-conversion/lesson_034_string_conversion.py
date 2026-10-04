"""String-conversion.

Strings are text, and text is written between quotes.

Run me:
    python 034-string-conversion/lesson_034_string_conversion.py
"""

from __future__ import annotations


def shout(text: str) -> str:
    """Return the text in upper case.

    Args:
        text: The text to shout.

    Returns:
        The same text, louder.

    Examples:
        >>> shout("hello")
        'HELLO'
    """
    return text.upper()


def count_words(sentence: str) -> int:
    """Count how many words are in a sentence.

    Args:
        sentence: The sentence to measure.

    Returns:
        The number of words.

    Examples:
        >>> count_words("a b c")
        3
    """
    return len(sentence.split())


def initials(name: str) -> str:
    """Return the initials of a full name.

    Args:
        name: A name such as ``"Ada Lovelace"``.

    Returns:
        The initials in upper case.

    Examples:
        >>> initials("Ada Lovelace")
        'AL'
    """
    return "".join(part[0] for part in name.split()).upper()


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(shout("hello"))
    print(count_words("one two three"))
    print(initials("Ada Lovelace"))


if __name__ == "__main__":
    main()
