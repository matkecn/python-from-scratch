"""Context-managers.

`with` sets something up and always tidies it away.

Run me:
    python 311-context-managers/lesson_311_context_managers.py
"""

from __future__ import annotations


from contextlib import contextmanager


@contextmanager
def announce(title: str):
    """Print a title before and after a block of code.

    Args:
        title: The title to print.

    Yields:
        The block to run.
    """
    print(f"start: {title}")
    yield
    print(f"end: {title}")


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    with announce("demo"):
        print("working")


if __name__ == "__main__":
    main()
