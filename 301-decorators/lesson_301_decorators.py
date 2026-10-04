"""Decorators.

A decorator wraps a function to add behaviour.

Run me:
    python 301-decorators/lesson_301_decorators.py
"""

from __future__ import annotations


from functools import wraps


def shouty(func):
    """Make a function's result louder.

    Args:
        func: The function to wrap.

    Returns:
        The wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Call the function and shout its result."""
        return str(func(*args, **kwargs)).upper()

    return wrapper


@shouty
def welcome(name: str) -> str:
    """Return a welcome message.

    Args:
        name: Who is arriving.

    Returns:
        A welcome message.
    """
    return f"welcome {name}"


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(welcome("Ada"))
    print(welcome.__name__)


if __name__ == "__main__":
    main()
