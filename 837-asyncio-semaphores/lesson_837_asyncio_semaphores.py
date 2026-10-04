"""Asyncio-semaphores.

Placeholder for **Asyncio-semaphores**. A later phase replaces this with a full lesson.

Run me:
    python 837-asyncio-semaphores/lesson_837_asyncio_semaphores.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"asyncio semaphores"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Asyncio-semaphores" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
