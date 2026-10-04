# 024 · Booleans

Booleans are just two values: `True` and `False`.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- Comparing makes a boolean
- `and`, `or` and `not` work on booleans
- `True` counts as 1

## 1. Run the example

```bash
python 024-booleans/lesson_024_booleans.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_024_booleans.py</code></summary>

```python
"""Booleans.

Booleans are just two values: `True` and `False`.

Run me:
    python 024-booleans/lesson_024_booleans.py
"""

from __future__ import annotations


def is_odd(number: int) -> bool:
    """Say whether a number is odd.

    Args:
        number: The number to check.

    Returns:
        ``True`` when the number is odd.

    Examples:
        >>> is_odd(3)
        True
    """
    return number % 2 == 1


def both_yes(first: bool, second: bool) -> bool:
    """Say whether both answers are yes.

    Args:
        first: The first yes or no.
        second: The second yes or no.

    Returns:
        ``True`` only when both are ``True``.

    Examples:
        >>> both_yes(True, False)
        False
    """
    return first and second


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(is_odd(3))
    print(both_yes(True, False))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 024-booleans
```

## 4. Open the notebook

```bash
jupyter notebook 024-booleans/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `boolean` | A value that is only `True` or `False` |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/introduction.html)

---

[← 023-complex-numbers](../023-complex-numbers/) · [Next: 025-none →](../025-none/)
