# 033 · Float-conversion

Floats are numbers with a decimal point.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- `float` stores decimal numbers
- Adding floats can be a tiny bit off
- `round` tidies the result

## 1. Run the example

```bash
python 033-float-conversion/lesson_033_float_conversion.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_033_float_conversion.py</code></summary>

```python
"""Float-conversion.

Floats are numbers with a decimal point.

Run me:
    python 033-float-conversion/lesson_033_float_conversion.py
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
pytest 033-float-conversion
```

## 4. Open the notebook

```bash
jupyter notebook 033-float-conversion/lesson.ipynb
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

[← 032-int-conversion](../032-int-conversion/) · [Next: 034-string-conversion →](../034-string-conversion/)
