"""Shlex.

`shlex` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 583-shlex/lesson_583_shlex.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import shlex

    return getattr(shlex, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names shlex offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import shlex

    return sorted(item for item in dir(shlex) if not item.startswith("_"))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(module_path())
    print(len(public_names()), 'public names')


if __name__ == "__main__":
    main()
