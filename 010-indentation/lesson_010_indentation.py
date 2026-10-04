"""Indentation.

Python does not use braces. It uses the spaces at the start of a line. Four
spaces is the usual width.

Run me:
    python 010-indentation/lesson_010_indentation.py
"""

from __future__ import annotations

WIDTH = 4


def indent_width(line: str) -> int:
    """Return how far a line is indented.

    Args:
        line: One line of code.

    Returns:
        The number of spaces before the first real character.

    Examples:
        >>> indent_width("    print(1)")
        4
        >>> indent_width("print(1)")
        0
    """
    return len(line) - len(line.lstrip(" "))


def opens_a_block(line: str) -> bool:
    """Say whether a line starts a new block.

    Args:
        line: One line of code.

    Returns:
        ``True`` when the line ends with a colon.

    Examples:
        >>> opens_a_block("if ready:")
        True
        >>> opens_a_block("    print(1)")
        False
    """
    return line.strip().endswith(":")


def block_depth(lines: list[str]) -> int:
    """Return how deep the deepest block goes.

    Args:
        lines: The lines of code.

    Returns:
        The largest indentation found, in spaces.

    Examples:
        >>> block_depth(["if a:", "    print(1)", "    for b in c:", "        print(2)"])
        8
    """
    return max((indent_width(line) for line in lines), default=0)


def count_statements(lines: list[str]) -> int:
    """Count the lines that actually do something.

    Blank lines, comments and closing brackets do not count.

    Args:
        lines: The lines of code.

    Returns:
        The number of real statements.

    Examples:
        >>> count_statements(["x = 1", "", "# note", "print(x)"])
        2
    """
    count = 0
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if text in {"}", "]", ")"}:
            continue
        count += 1
    return count


def main() -> None:
    """Measure a small piece of indented code."""
    lines = [
        "total = 0",
        "for number in [1, 2, 3]:",
        "    total += number",
        "print(total)",
    ]
    print(f"deepest block: {block_depth(lines)} spaces")
    print(f"statements: {count_statements(lines)}")


if __name__ == "__main__":
    main()
