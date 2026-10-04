"""Web-framework-concepts.

Placeholder for **Web-framework-concepts**. A later phase replaces this with a full lesson.

Run me:
    python 924-web-framework-concepts/lesson_924_web_framework_concepts.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"web framework concepts"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Web-framework-concepts" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
