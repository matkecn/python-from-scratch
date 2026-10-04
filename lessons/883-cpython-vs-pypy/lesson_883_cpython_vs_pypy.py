"""Cpython-vs-pypy.

Placeholder for **Cpython-vs-pypy**. A later phase replaces this with a full lesson.

Run me:
    python 883-cpython-vs-pypy/lesson_883_cpython_vs_pypy.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"cpython vs pypy"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Cpython-vs-pypy" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
