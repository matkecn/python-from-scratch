"""Welcome to Python.

The shortest useful program in any language is one line. This is ours.

Run me:
    python 000-welcome/lesson_000_welcome.py
"""

from __future__ import annotations


def hello_world() -> str:
    """Return the classic first line of programming.

    Returns:
        The text ``"Hello, world!"``.

    Examples:
        >>> hello_world()
        'Hello, world!'
    """
    return "Hello, world!"


def greet(name: str) -> str:
    """Return a greeting for one person.

    Args:
        name: Who to greet. An empty name falls back to ``"world"``.

    Returns:
        A friendly greeting.

    Examples:
        >>> greet("Ada")
        'Hello, Ada!'
        >>> greet("")
        'Hello, world!'
    """
    who = name or "world"
    return f"Hello, {who}!"


def main() -> None:
    """Print the classic line, then a personal one."""
    print(hello_world())
    print(greet("Ada"))


if __name__ == "__main__":
    main()
