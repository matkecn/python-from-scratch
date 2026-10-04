"""Line-profiler.

Placeholder for **Line-profiler**. A later phase replaces this with a full lesson.

Run me:
    python 847-line-profiler/lesson_847_line_profiler.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"line profiler"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Line-profiler" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
