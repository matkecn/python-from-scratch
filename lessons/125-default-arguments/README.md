# 125 · Default-arguments

Arguments are the values you hand to a function.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Positional arguments go by position
- Keyword arguments go by name
- Defaults fill the blanks

## 1. Run the example

```bash
python 125-default-arguments/lesson_125_default_arguments.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_125_default_arguments.py</code></summary>

```python
"""Default-arguments.

Arguments are the values you hand to a function.

Run me:
    python 125-default-arguments/lesson_125_default_arguments.py
"""

from __future__ import annotations


def greet(name: str, greeting: str = "Hello") -> str:
    """Build a greeting.

    Args:
        name: Who to greet.
        greeting: The word to use first.

    Returns:
        The full greeting.

    Examples:
        >>> greet("Ada")
        'Hello, Ada'
        >>> greet("Ada", greeting="Hi")
        'Hi, Ada'
    """
    return f"{greeting}, {name}"


def total_price(cost: float, quantity: int, *, tax: float = 0.0) -> float:
    """Work out a price with tax.

    Args:
        cost: The price of one item.
        quantity: How many items.
        tax: The tax rate, so ``0.2`` means twenty percent.

    Returns:
        The full price, rounded to two decimals.
    """
    return round(cost * quantity * (1 + tax), 2)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(greet("Ada"))
    print(total_price(2.5, 3, tax=0.2))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 125-default-arguments
```

## 4. Open the notebook

```bash
jupyter notebook 125-default-arguments/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `parameter` | The name in the function definition |
| `argument` | The value you pass in |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 124-keyword-arguments](../124-keyword-arguments/) · [Next: 126-positional-only →](../126-positional-only/)
