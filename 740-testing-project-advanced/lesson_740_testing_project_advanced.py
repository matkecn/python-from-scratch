"""Testing-project-advanced.

Placeholder for **Testing-project-advanced**. A later phase replaces this with a full lesson.

Run me:
    python 740-testing-project-advanced/lesson_740_testing_project_advanced.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"testing project advanced"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Testing-project-advanced" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
