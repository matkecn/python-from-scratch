"""Re.

`re` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 548-re/lesson_548_re.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import re

    return getattr(re, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names re offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import re

    return sorted(item for item in dir(re) if not item.startswith("_"))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(module_path())
    print(len(public_names()), 'public names')


if __name__ == "__main__":
    main()
