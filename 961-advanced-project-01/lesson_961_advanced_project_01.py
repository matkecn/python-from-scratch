"""Advanced-project-01.

Placeholder for **Advanced-project-01**. A later phase replaces this with a full lesson.

Run me:
    python 961-advanced-project-01/lesson_961_advanced_project_01.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"advanced project 01"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Advanced-project-01" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
