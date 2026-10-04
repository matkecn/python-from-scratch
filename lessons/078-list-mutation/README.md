# 078 · List-mutation

A list keeps many values in order.

**Section** Lists, tuples, sets and dictionaries · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Make a list with `[ ]`
- Count items with `len`
- Add to the end with `append`

## 1. Run the example

```bash
python 078-list-mutation/lesson_078_list_mutation.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_078_list_mutation.py</code></summary>

```python
"""List-mutation.

A list keeps many values in order.

Run me:
    python 078-list-mutation/lesson_078_list_mutation.py
"""

from __future__ import annotations


def add_up(numbers: list[int]) -> int:
    """Add every number in a list.

    Args:
        numbers: The numbers to add.

    Returns:
        The total.

    Examples:
        >>> add_up([1, 2, 3])
        6
    """
    return sum(numbers)


def biggest(numbers: list[int]) -> int:
    """Return the largest number in a list.

    Args:
        numbers: A list that is not empty.

    Returns:
        The largest number.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> biggest([4, 9, 2])
        9
    """
    if not numbers:
        raise ValueError("list is empty")
    return max(numbers)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(add_up([1, 2, 3]))
    print(biggest([4, 9, 2]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 078-list-mutation
```

## 4. Open the notebook

```bash
jupyter notebook 078-list-mutation/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `list` | An ordered box that can grow and shrink |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datastructures.html)

---

[← 077-list-copying](../077-list-copying/) · [Next: 079-list-unpacking →](../079-list-unpacking/)
