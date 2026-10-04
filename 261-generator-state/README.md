# 261 · Generator-state

A generator makes values on demand and forgets them after.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- `yield` pauses a function
- Generators are lazy
- Loop over them like any list

## 1. Run the example

```bash
python 261-generator-state/lesson_261_generator_state.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_261_generator_state.py</code></summary>

```python
"""Generator-state.

A generator makes values on demand and forgets them after.

Run me:
    python 261-generator-state/lesson_261_generator_state.py
"""

from __future__ import annotations


def count_up(limit: int):
    """Yield the numbers from one to a limit.

    Args:
        limit: The last number to give.

    Yields:
        Each number in turn.

    Examples:
        >>> list(count_up(3))
        [1, 2, 3]
    """
    for number in range(1, limit + 1):
        yield number


def evens(limit: int):
    """Yield only the even numbers below a limit.

    Args:
        limit: The limit to stop at.

    Yields:
        Each even number in turn.
    """
    for number in range(0, limit, 2):
        yield number


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(list(count_up(3)))
    print(list(evens(7)))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 261-generator-state
```

## 4. Open the notebook

```bash
jupyter notebook 261-generator-state/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `generator` | A function that gives values one at a time |
| `yield` | Pause and hand out one value |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 260-generator-functions](../260-generator-functions/) · [Next: 262-send →](../262-send/)
