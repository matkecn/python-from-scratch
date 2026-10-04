# 905 · Cli-password-generator

A generator makes values on demand and forgets them after.

**Section** Practical Python applications · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `yield` pauses a function
- Generators are lazy
- Loop over them like any list

## 1. Run the example

```bash
python 905-cli-password-generator/lesson_905_cli_password_generator.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_905_cli_password_generator.py</code></summary>

```python
"""Cli-password-generator.

A generator makes values on demand and forgets them after.

Run me:
    python 905-cli-password-generator/lesson_905_cli_password_generator.py
"""

from __future__ import annotations


def count_up(limit: int):
    """Yield the numbers from one to a limit.

    Args:
        limit: The last number to give.

    Yields:
        Each number in turn.

    Examples:
        >>> list(count_up(3))
        [1, 2, 3]
    """
    for number in range(1, limit + 1):
        yield number


def evens(limit: int):
    """Yield only the even numbers below a limit.

    Args:
        limit: The limit to stop at.

    Yields:
        Each even number in turn.
    """
    for number in range(0, limit, 2):
        yield number


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(list(count_up(3)))
    print(list(evens(7)))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 905-cli-password-generator
```

## 4. Open the notebook

```bash
jupyter notebook 905-cli-password-generator/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `generator` | A function that gives values one at a time |
| `yield` | Pause and hand out one value |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 904-cli-notes](../904-cli-notes/) · [Next: 906-cli-file-manager →](../906-cli-file-manager/)
