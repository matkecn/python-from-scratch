# 351 · Type-hints

Type hints describe what a function expects and gives back.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Write `: int` after a parameter
- `-> str` after the parameters
- Hints help readers and checkers

## 1. Run the example

```bash
python 351-type-hints/lesson_351_type_hints.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_351_type_hints.py</code></summary>

```python
"""Type-hints.

Type hints describe what a function expects and gives back.

Run me:
    python 351-type-hints/lesson_351_type_hints.py
"""

from __future__ import annotations


def double(number: int) -> int:
    """Double a number.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    return number * 2


def average(numbers: list[float]) -> float:
    """Return the mean of some numbers.

    Args:
        numbers: A non empty list of numbers.

    Returns:
        The mean.
    """
    return sum(numbers) / len(numbers)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(double(4))
    print(average([1.0, 2.0]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 351-type-hints
```

## 4. Open the notebook

```bash
jupyter notebook 351-type-hints/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `type hint` | A note about the type of a value |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 350-advanced-python-project](../350-advanced-python-project/) · [Next: 352-typing →](../352-typing/)
