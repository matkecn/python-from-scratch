# 131 · Multiple-return-values

`return` sends a value back to whoever called the function.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- `return` ends the function
- No `return` means `None`
- Return a tuple to return many values

## 1. Run the example

```bash
python 131-multiple-return-values/lesson_131_multiple_return_values.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_131_multiple_return_values.py</code></summary>

```python
"""Multiple-return-values.

`return` sends a value back to whoever called the function.

Run me:
    python 131-multiple-return-values/lesson_131_multiple_return_values.py
"""

from __future__ import annotations


def divide(pie: int, people: int) -> tuple[int, int]:
    """Share a pie as evenly as possible.

    Args:
        pie: How many pieces the pie has.
        people: How many people share it.

    Returns:
        Each person's share and the pieces left over.

    Raises:
        ValueError: If there are no people.

    Examples:
        >>> divide(8, 3)
        (2, 2)
    """
    if people == 0:
        raise ValueError("need at least one person")
    return divmod(pie, people)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    share, left = divide(8, 3)
    print(f"each gets {share}, {left} left")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 131-multiple-return-values
```

## 4. Open the notebook

```bash
jupyter notebook 131-multiple-return-values/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `return` | Hand a value back to the caller |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 130-return](../130-return/) · [Next: 132-function-annotations →](../132-function-annotations/)
