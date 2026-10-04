"""Beginner-project-04.

Placeholder for **Beginner-project-04**. A later phase replaces this with a full lesson.

Run me:
    python 954-beginner-project-04/lesson_954_beginner_project_04.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"beginner project 04"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Beginner-project-04" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
