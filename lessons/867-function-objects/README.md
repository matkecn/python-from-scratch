# 867 · Function-objects

A function is a named recipe you can run again and again.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Define one with `def`
- Inputs are parameters
- `return` sends a value back

## 1. Run the example

```bash
python 867-function-objects/lesson_867_function_objects.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_867_function_objects.py</code></summary>

```python
"""Function-objects.

A function is a named recipe you can run again and again.

Run me:
    python 867-function-objects/lesson_867_function_objects.py
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
pytest 867-function-objects
```

## 4. Open the notebook

```bash
jupyter notebook 867-function-objects/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `function` | A named recipe that takes inputs and gives an answer |
| `return` | The value a function hands back |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 866-frame-objects](../866-frame-objects/) · [Next: 868-module-objects →](../868-module-objects/)
