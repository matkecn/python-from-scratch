# 139 · Higher-order-functions

A function is a named recipe you can run again and again.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Define one with `def`
- Inputs are parameters
- `return` sends a value back

## 1. Run the example

```bash
python 139-higher-order-functions/lesson_139_higher_order_functions.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_139_higher_order_functions.py</code></summary>

```python
"""Higher-order-functions.

A function is a named recipe you can run again and again.

Run me:
    python 139-higher-order-functions/lesson_139_higher_order_functions.py
"""

from __future__ import annotations


def area(width: float, height: float) -> float:
    """Return the area of a rectangle.

    Args:
        width: How wide it is.
        height: How tall it is.

    Returns:
        The area.

    Examples:
        >>> area(2.0, 3.0)
        6.0
    """
    return width * height


def describe(width: float, height: float) -> str:
    """Describe a rectangle in words.

    Args:
        width: How wide it is.
        height: How tall it is.

    Returns:
        A short sentence.
    """
    return f"A rectangle of {area(width, height)} square units."


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(area(2.0, 3.0))
    print(describe(2.0, 3.0))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 139-higher-order-functions
```

## 4. Open the notebook

```bash
jupyter notebook 139-higher-order-functions/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `function` | A named recipe that takes inputs and gives an answer |
| `return` | The value a function hands back |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 138-recursion](../138-recursion/) · [Next: 140-first-class-functions →](../140-first-class-functions/)
