"""Custom-awaitable.

Placeholder for **Custom-awaitable**. A later phase replaces this with a full lesson.

Run me:
    python 448-custom-awaitable/lesson_448_custom_awaitable.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"custom awaitable"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Custom-awaitable" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
