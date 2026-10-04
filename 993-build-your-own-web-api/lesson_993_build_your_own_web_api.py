"""Build-your-own-web-api.

Placeholder for **Build-your-own-web-api**. A later phase replaces this with a full lesson.

Run me:
    python 993-build-your-own-web-api/lesson_993_build_your_own_web_api.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"build your own web api"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Build-your-own-web-api" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
