# 010 · Indentation

Indentation is how Python shows which lines belong together.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Blocks start with a `:` and end when the indentation shrinks
- Measure indentation with `len`
- Keep blocks at one consistent width

## 1. Run the example

```bash
python 010-indentation/lesson_010_indentation.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_010_indentation.py</code></summary>

```python
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
```

</details>

## 3. Run the tests

```bash
pytest 010-indentation
```

## 4. Open the notebook

```bash
jupyter notebook 010-indentation/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `block` | A group of lines that belong together |
| `indentation` | The spaces at the start of a line |

## Your turn

1. Rewrite a four space block with two spaces and see if Python complains.
2. Find the deepest block in a file you already wrote.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 009-comments](../009-comments/) · [Next: 011-print →](../011-print/)
