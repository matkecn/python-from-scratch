# 009 · Comments

Comments are notes for humans. Python ignores them.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Write a note with `#`
- Know that a docstring is a comment with power
- See why comments should say why, not what

## 1. Run the example

```bash
python 009-comments/lesson_009_comments.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_009_comments.py</code></summary>

```python
"""Comments.

A comment starts with ``#`` and ends at the end of the line. Python never
runs it. People do.

Run me:
    python 009-comments/lesson_009_comments.py
"""

from __future__ import annotations

COMMENT = "#"


def is_comment(line: str) -> bool:
    """Say whether a line is only a comment.

    Args:
        line: One line of code.

    Returns:
        ``True`` when the line starts with ``#``.

    Examples:
        >>> is_comment("# a note")
        True
        >>> is_comment("total = 1  # a note")
        False
    """
    return line.strip().startswith(COMMENT)


def strip_comment(line: str) -> str:
    """Remove the comment from a line of code.

    This is a simple lesson, so it removes everything after the first ``#``.
    A ``#`` inside a string is left alone by Python but not by this helper.

    Args:
        line: One line of code.

    Returns:
        The code part of the line, with spaces trimmed.

    Examples:
        >>> strip_comment("total = 1  # add one")
        'total = 1'
        >>> strip_comment("# only a note")
        ''
    """
    return line.split(COMMENT, 1)[0].strip()


def count_comments(lines: list[str]) -> int:
    """Count how many of these lines are pure comments.

    Args:
        lines: The lines to look at.

    Returns:
        The number of comment lines.

    Examples:
        >>> count_comments(["# one", "x = 1", "# two"])
        2
    """
    return sum(1 for line in lines if is_comment(line))


def why_not_what() -> str:
    """Return the rule of thumb for writing comments.

    Returns:
        A one line reminder.

    Examples:
        >>> "why" in why_not_what()
        True
    """
    return "Say why you did it. The code already says what it does."


def main() -> None:
    """Look at a few lines of commented code."""
    lines = [
        "# This file counts birds.",
        "birds = 3  # we saw three today",
        "print(birds)",
    ]
    print(f"{count_comments(lines)} pure comment lines")
    for line in lines:
        print(f"{strip_comment(line)!r}")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 009-comments
```

## 4. Open the notebook

```bash
jupyter notebook 009-comments/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `comment` | A note for people that Python skips |
| `docstring` | The first string in a file or function |

## Your turn

1. Take a file you wrote and delete every comment that only says what.
2. Write a comment that explains why a strange value is needed.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 008-python-files](../008-python-files/) · [Next: 010-indentation →](../010-indentation/)
