"""Property-as-descriptor.

Placeholder for **Property-as-descriptor**. A later phase replaces this with a full lesson.

Run me:
    python 327-property-as-descriptor/lesson_327_property_as_descriptor.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"property as descriptor"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Property-as-descriptor" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
