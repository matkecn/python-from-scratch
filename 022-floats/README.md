# 022 · Floats

Floats are numbers with a decimal point.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- `float` stores decimal numbers
- Adding floats can be a tiny bit off
- `round` tidies the result

## 1. Run the example

```bash
python 022-floats/lesson_022_floats.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_022_floats.py</code></summary>

```python
"""Floats.

Floats are numbers with a decimal point.

Run me:
    python 022-floats/lesson_022_floats.py
"""

from __future__ import annotations


def average(numbers: list[float]) -> float:
    """Return the mean of some numbers.

    Args:
        numbers: The numbers to average. Must not be empty.

    Returns:
        The mean, rounded to two decimal places.

    Raises:
        ValueError: If ``numbers`` is empty.

    Examples:
        >>> average([1.0, 2.0, 4.0])
        2.33
    """
    if not numbers:
        raise ValueError("need at least one number")
    return round(sum(numbers) / len(numbers), 2)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(average([1.0, 2.0, 4.0]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 022-floats
```

## 4. Open the notebook

```bash
jupyter notebook 022-floats/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `float` | A number with a decimal point, such as 1.5 |

## Your turn

1. Round the average to one decimal place instead of two.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/introduction.html)

---

[← 021-integers](../021-integers/) · [Next: 023-complex-numbers →](../023-complex-numbers/)
