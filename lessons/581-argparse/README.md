# 581 · argparse

`argparse` reads command line arguments for you.

**Section** Command line tools and logging · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Describe each argument
- Read them from `sys.argv`
- `--help` comes free

## 1. Run the example

```bash
python 581-argparse/lesson_581_argparse.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_581_argparse.py</code></summary>

```python
"""argparse.

`argparse` reads command line arguments for you.

Run me:
    python 581-argparse/lesson_581_argparse.py
"""

from __future__ import annotations


import argparse


def build_parser() -> argparse.ArgumentParser:
    """Make the argument reader for a tiny tool.

    Returns:
        A parser that understands ``name`` and ``--times``.
    """
    parser = argparse.ArgumentParser(description="Say hello a few times.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--times", type=int, default=1, help="how many greetings")
    return parser


def greeting_for(name: str, times: int) -> str:
    """Build the greeting lines.

    Args:
        name: Who to greet.
        times: How many lines to make.

    Returns:
        The lines joined by newlines.
    """
    return "\n".join(f"Hello, {name}!" for _ in range(times))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(greeting_for("Ada", 2))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 581-argparse
```

## 4. Open the notebook

```bash
jupyter notebook 581-argparse/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `argument` | A value typed on the command line |

## Read more

- [`argparse` module docs](https://docs.python.org/3/library/argparse.html)

---

[← 580-stdlib-review](../580-stdlib-review/) · [Next: 582-getopt →](../582-getopt/)
