# 974 · Iterator-challenges

Iterators hand out one value at a time.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- `for` asks for values with `next`
- `iter` makes an iterator
- `StopIteration` ends it

## 1. Run the example

```bash
python 974-iterator-challenges/lesson_974_iterator_challenges.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_974_iterator_challenges.py</code></summary>

```python
"""Iterator-challenges.

Iterators hand out one value at a time.

Run me:
    python 974-iterator-challenges/lesson_974_iterator_challenges.py
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
pytest 974-iterator-challenges
```

## 4. Open the notebook

```bash
jupyter notebook 974-iterator-challenges/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `iterator` | A thing that gives values one by one |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 973-functional-challenges](../973-functional-challenges/) · [Next: 975-generator-challenges →](../975-generator-challenges/)
