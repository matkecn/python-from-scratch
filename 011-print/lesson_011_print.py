"""Print.

`print` is for people. `return` is for code. A function that returns a value
can be printed later, reused and tested.

Run me:
    python 011-print/lesson_011_print.py
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


def show(text: str, times: int = 1) -> None:
    """Print some text a number of times.

    Args:
        text: The text to print.
        times: How many lines to print.
    """
    for _ in range(times):
        print(text)


def join_numbers(numbers: list[int]) -> str:
    """Return numbers as one line, separated by dashes.

    Args:
        numbers: The numbers to join.

    Returns:
        A single line of text.

    Examples:
        >>> join_numbers([1, 2, 3])
        '1 - 2 - 3'
    """
    return " - ".join(str(number) for number in numbers)


def main() -> None:
    """Show printing and returning side by side."""
    print(shout("hello"))
    show("again", times=2)
    print(join_numbers([1, 2, 3]))


if __name__ == "__main__":
    main()
