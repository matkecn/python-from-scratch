# 015 · Assignment

`=` assigns, `==` compares. Learning the difference saves hours.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- `=` puts a value in a name
- `==` asks whether two values match
- `+=` and friends update in place

## 1. Run the example

```bash
python 015-assignment/lesson_015_assignment.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_015_assignment.py</code></summary>

```python
"""Assignment.

``=`` copies a value into a name. ``==`` asks a question. Mixing them up is the
most common small bug in Python.

Run me:
    python 015-assignment/lesson_015_assignment.py
"""

from __future__ import annotations


def are_equal(first: int, second: int) -> bool:
    """Say whether two numbers match.

    Args:
        first: The number on the left.
        second: The number on the right.

    Returns:
        ``True`` when they are equal.

    Examples:
        >>> are_equal(2, 2)
        True
        >>> are_equal(2, 3)
        False
    """
    return first == second


def add_to_total(total: int, amount: int = 1) -> int:
    """Add to a running total.

    Args:
        total: The total so far.
        amount: How much to add.

    Returns:
        The new total.
    """
    total += amount
    return total


def chain() -> tuple[int, int, int]:
    """Show that one value can wear three names.

    Returns:
        Three copies of the same number.

    Examples:
        >>> chain()
        (7, 7, 7)
    """
    first = second = third = 7
    return first, second, third


def count_down(start: int) -> list[int]:
    """Return the numbers from start down to one.

    Args:
        start: The number to start from.

    Returns:
        The numbers, largest first.

    Examples:
        >>> count_down(3)
        [3, 2, 1]
    """
    numbers = list(range(start, 0, -1))
    return numbers


def main() -> None:
    """Compare, then update."""
    total = 0
    for amount in [5, 3, 2]:
        total = add_to_total(total, amount)
    print(f"total is {total}, equal to 10? {are_equal(total, 10)}")
    print(count_down(3))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 015-assignment
```

## 4. Open the notebook

```bash
jupyter notebook 015-assignment/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `assignment` | Putting a value into a name |
| `augmented assignment` | An update such as `total += 1` |

## Your turn

1. Write a line that uses `=` and the same line with `==`, then predict each result.
2. Add a `halve` function that divides a total in place.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 014-naming](../014-naming/) · [Next: 016-expressions →](../016-expressions/)
