# 141 · Lambda

A lambda is a tiny function with no name and no body.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- `lambda x: ...` makes a small function
- Perfect for sort keys
- Use `def` for anything longer

## 1. Run the example

```bash
python 141-lambda/lesson_141_lambda.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_141_lambda.py</code></summary>

```python
"""Lambda.

A lambda is a tiny function with no name and no body.

Run me:
    python 141-lambda/lesson_141_lambda.py
"""

from __future__ import annotations


def add_tax(price: float) -> float:
    """Add twenty percent tax to a price.

    Args:
        price: The price before tax.

    Returns:
        The price with tax.

    Examples:
        >>> add_tax(10.0)
        12.0
    """
    with_tax = lambda value: round(value * 1.2, 2)
    return with_tax(price)


def by_length(words: list[str]) -> list[str]:
    """Sort words from longest to shortest.

    Args:
        words: The words to sort.

    Returns:
        A new sorted list.
    """
    return sorted(words, key=lambda word: len(word), reverse=True)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(add_tax(10.0))
    print(by_length(["pear", "fig", "banana"]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 141-lambda
```

## 4. Open the notebook

```bash
jupyter notebook 141-lambda/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `lambda` | A small nameless function |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 140-first-class-functions](../140-first-class-functions/) · [Next: 142-map →](../142-map/)
