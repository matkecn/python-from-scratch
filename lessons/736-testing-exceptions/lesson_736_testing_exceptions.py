"""Testing-exceptions.

Exceptions are how Python complains about problems.

Run me:
    python 736-testing-exceptions/lesson_736_testing_exceptions.py
"""

from __future__ import annotations


def parse_age(text: str) -> int:
    """Turn text into an age.

    Args:
        text: The text to read.

    Returns:
        The age as a whole number.

    Raises:
        ValueError: If the text is not a whole number.

    Examples:
        >>> parse_age("12")
        12
    """
    try:
        return int(text)
    except ValueError as error:
        raise ValueError(f"age must be a whole number: {text!r}") from error


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(parse_age("12"))
    try:
        print(parse_age("old"))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
