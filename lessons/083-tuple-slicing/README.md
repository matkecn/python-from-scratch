# 083 · Tuple-slicing

A tuple is a list that cannot be changed.

**Section** Lists, tuples, sets and dictionaries · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Make a tuple with `( )`
- Unpack it in one line
- Safe to use as a dictionary key

## 1. Run the example

```bash
python 083-tuple-slicing/lesson_083_tuple_slicing.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_083_tuple_slicing.py</code></summary>

```python
"""Tuple-slicing.

A tuple is a list that cannot be changed.

Run me:
    python 083-tuple-slicing/lesson_083_tuple_slicing.py
"""

from __future__ import annotations


def first_and_last(numbers: tuple[int, ...]) -> tuple[int, int]:
    """Return the first and last number of a tuple.

    Args:
        numbers: A tuple with at least one number.

    Returns:
        The first and last number.

    Raises:
        ValueError: If the tuple is empty.

    Examples:
        >>> first_and_last((3, 4, 5))
        (3, 5)
    """
    if not numbers:
        raise ValueError("tuple is empty")
    return numbers[0], numbers[-1]


def swap(pair: tuple[int, int]) -> tuple[int, int]:
    """Swap the two numbers in a pair.

    Args:
        pair: Two numbers.

    Returns:
        The pair, backwards.

    Examples:
        >>> swap((1, 2))
        (2, 1)
    """
    left, right = pair
    return right, left


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(first_and_last((3, 4, 5)))
    print(swap((1, 2)))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 083-tuple-slicing
```

## 4. Open the notebook

```bash
jupyter notebook 083-tuple-slicing/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `tuple` | A short, unchangeable sequence |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datastructures.html)

---

[← 082-tuple-indexing](../082-tuple-indexing/) · [Next: 084-tuple-methods →](../084-tuple-methods/)
