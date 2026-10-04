"""Conditional-expressions.

Placeholder for **Conditional-expressions**. A later phase replaces this with a full lesson.

Run me:
    python 059-conditional-expressions/lesson_059_conditional_expressions.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"conditional expressions"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Conditional-expressions" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
