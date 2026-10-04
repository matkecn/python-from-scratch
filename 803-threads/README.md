# 803 · Threads

Threads run many tasks at once inside one program.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- A thread is a helper of the program
- Share data carefully
- Use a lock when sharing

## 1. Run the example

```bash
python 803-threads/lesson_803_threads.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_803_threads.py</code></summary>

```python
"""Threads.

Threads run many tasks at once inside one program.

Run me:
    python 803-threads/lesson_803_threads.py
"""

from __future__ import annotations


from concurrent.futures import ThreadPoolExecutor


def double(number: int) -> int:
    """Double a number.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    return number * 2


def double_all(numbers: list[int]) -> list[int]:
    """Double many numbers using a pool of threads.

    Args:
        numbers: The numbers to double.

    Returns:
        The doubled numbers, in order.
    """
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(double, numbers))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(double_all([1, 2, 3]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 803-threads
```

## 4. Open the notebook

```bash
jupyter notebook 803-threads/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `thread` | A helper that runs at the same time as the program |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 802-processes](../802-processes/) · [Next: 804-threading →](../804-threading/)
