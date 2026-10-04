# 149 · Closures

A closure is a function that remembers names from around it.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Inner functions can read outer names
- `nonlocal` changes an outer name
- Great for counters

## 1. Run the example

```bash
python 149-closures/lesson_149_closures.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_149_closures.py</code></summary>

```python
"""Closures.

A closure is a function that remembers names from around it.

Run me:
    python 149-closures/lesson_149_closures.py
"""

from __future__ import annotations


from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    """Make a counter that remembers how often it was called.

    Args:
        start: The number to start from.

    Returns:
        A function that counts 1, 2, 3 and so on from ``start``.

    Examples:
        >>> tick = make_counter()
        >>> tick(), tick()
        (1, 2)
    """
    count = start

    def tick() -> int:
        """Add one and return the new count."""
        nonlocal count
        count += 1
        return count

    return tick


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    tick = make_counter()
    print(tick(), tick(), tick())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 149-closures
```

## 4. Open the notebook

```bash
jupyter notebook 149-closures/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `closure` | A function that remembers names from around it |
| `nonlocal` | Reach one scope out to change a name |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 148-partial](../148-partial/) · [Next: 150-function-factories →](../150-function-factories/)
