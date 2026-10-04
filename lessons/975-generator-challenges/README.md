# 975 · Generator-challenges

A generator makes values on demand and forgets them after.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- `yield` pauses a function
- Generators are lazy
- Loop over them like any list

## 1. Run the example

```bash
python 975-generator-challenges/lesson_975_generator_challenges.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_975_generator_challenges.py</code></summary>

```python
"""Generator-challenges.

A generator makes values on demand and forgets them after.

Run me:
    python 975-generator-challenges/lesson_975_generator_challenges.py
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
pytest 975-generator-challenges
```

## 4. Open the notebook

```bash
jupyter notebook 975-generator-challenges/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `generator` | A function that gives values one at a time |
| `yield` | Pause and hand out one value |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 974-iterator-challenges](../974-iterator-challenges/) · [Next: 976-file-challenges →](../976-file-challenges/)
