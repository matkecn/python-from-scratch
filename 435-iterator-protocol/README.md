# 435 · Iterator-protocol

Iterators hand out one value at a time.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `for` asks for values with `next`
- `iter` makes an iterator
- `StopIteration` ends it

## 1. Run the example

```bash
python 435-iterator-protocol/lesson_435_iterator_protocol.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_435_iterator_protocol.py</code></summary>

```python
"""Iterator-protocol.

Iterators hand out one value at a time.

Run me:
    python 435-iterator-protocol/lesson_435_iterator_protocol.py
"""

from __future__ import annotations


def count_to(limit: int) -> int:
    """Count from one to a limit and return how many numbers there were.

    Args:
        limit: The last number to count.

    Returns:
        The amount of numbers counted.

    Examples:
        >>> count_to(3)
        3
    """
    how_many = 0
    for _ in range(limit):
        how_many += 1
    return how_many


def take_first(items: list[int], how_many: int) -> list[int]:
    """Take the first few items from a list using an iterator.

    Args:
        items: Where to take them from.
        how_many: How many to take.

    Returns:
        The items that were taken.
    """
    picker = iter(items)
    return [next(picker) for _ in range(how_many)]


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(count_to(3))
    print(take_first([9, 8, 7], 2))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 435-iterator-protocol
```

## 4. Open the notebook

```bash
jupyter notebook 435-iterator-protocol/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `iterator` | A thing that gives values one by one |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 434-context-protocol](../434-context-protocol/) · [Next: 436-descriptor-protocol →](../436-descriptor-protocol/)
