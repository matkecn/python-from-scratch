"""Builtins.

Open Python and type `print`. It was already there. Everything in this lesson
was also already there, waiting for you.

Run me:
    python 019-builtins/lesson_019_builtins.py
"""

from __future__ import annotations

import builtins

HANDY = ("len", "sum", "min", "max", "sorted", "round", "abs", "print")


def builtin_names() -> list[str]:
    """Return every built in name Python offers.

    Returns:
        A sorted list of names.
    """
    return sorted(name for name in dir(builtins) if not name.startswith("_"))


def exists(name: str) -> bool:
    """Say whether Python has a built in with this name.

    Args:
        name: The name to look for.

    Returns:
        ``True`` when Python has it.

    Examples:
        >>> exists("len")
        True
        >>> exists("banana")
        False
    """
    return hasattr(builtins, name)


def use_these() -> str:
    """Use several built in functions and describe the results.

    Returns:
        A short report.

    Examples:
        >>> "3" in use_these()
        True
    """
    numbers = [4, 1, 3]
    return (
        f"len is {len(numbers)}, sum is {sum(numbers)}, "
        f"min is {min(numbers)}, max is {max(numbers)}, sorted is {sorted(numbers)}"
    )


def abilities(value: object) -> list[str]:
    """Return what an object can do.

    Args:
        value: Anything, such as a list.

    Returns:
        The public names the object has.

    Examples:
        >>> "append" in abilities([])
        True
    """
    return sorted(name for name in dir(value) if not name.startswith("_"))


def main() -> None:
    """Show what comes free with Python."""
    print(f"{len(builtin_names())} built in names")
    print(use_these())
    print(f"a list can: {', '.join(abilities([])[:5])} ...")


if __name__ == "__main__":
    main()
