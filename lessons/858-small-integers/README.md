# 858 · Small integers

Integers are whole numbers with no decimal part.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- `int` holds whole numbers
- Python integers never overflow
- `//` divides and drops the rest

## 1. Run the example

```bash
python 858-small-integers/lesson_858_small_integers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_858_small_integers.py</code></summary>

```python
"""Small integers.

Integers are whole numbers with no decimal part.

Run me:
    python 858-small-integers/lesson_858_small_integers.py
"""

from __future__ import annotations


def whole_pairs(count: int) -> int:
    """Return how many whole pairs a count makes.

    Args:
        count: How many things there are.

    Returns:
        The number of whole pairs.

    Examples:
        >>> whole_pairs(7)
        3
    """
    return count // 2


def is_even(number: int) -> bool:
    """Say whether a number divides by two with nothing left over.

    Args:
        number: The number to check.

    Returns:
        ``True`` when the number is even.

    Examples:
        >>> is_even(4)
        True
    """
    return number % 2 == 0


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(whole_pairs(7))
    print(is_even(4))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 858-small-integers
```

## 4. Open the notebook

```bash
jupyter notebook 858-small-integers/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `integer` | A whole number such as 0, 1 or -42 |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 857-interning](../857-interning/) · [Next: 859-string-interning →](../859-string-interning/)
