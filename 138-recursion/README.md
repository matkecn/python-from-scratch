# 138 · Recursion

Recursion is a function calling itself with a smaller problem.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Every recursion needs a stopping point
- The base case comes first
- Recursion follows the shape of the data

## 1. Run the example

```bash
python 138-recursion/lesson_138_recursion.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_138_recursion.py</code></summary>

```python
"""Recursion.

Recursion is a function calling itself with a smaller problem.

Run me:
    python 138-recursion/lesson_138_recursion.py
"""

from __future__ import annotations


def factorial(number: int) -> int:
    """Return the product of all numbers up to ``number``.

    Args:
        number: A whole number of 0 or more.

    Returns:
        The factorial.

    Examples:
        >>> factorial(5)
        120
    """
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def total_length(text: str) -> int:
    """Return how many characters a string holds.

    Args:
        text: The string to measure.

    Returns:
        The number of characters.
    """
    if not text:
        return 0
    return len(text[0]) + total_length(text[1:])


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(factorial(5))
    print(total_length("hello"))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 138-recursion
```

## 4. Open the notebook

```bash
jupyter notebook 138-recursion/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `recursion` | A function that calls itself |
| `base case` | The simple answer that stops the recursion |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 137-nonlocal](../137-nonlocal/) · [Next: 139-higher-order-functions →](../139-higher-order-functions/)
