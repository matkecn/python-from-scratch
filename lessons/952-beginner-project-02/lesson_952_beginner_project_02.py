"""Beginner-project-02.

Placeholder for **Beginner-project-02**. A later phase replaces this with a full lesson.

Run me:
    python 952-beginner-project-02/lesson_952_beginner_project_02.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"beginner project 02"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Beginner-project-02" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
