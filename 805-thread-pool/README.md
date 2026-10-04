# 805 · Thread-pool

Threads run many tasks at once inside one program.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- A thread is a helper of the program
- Share data carefully
- Use a lock when sharing

## 1. Run the example

```bash
python 805-thread-pool/lesson_805_thread_pool.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_805_thread_pool.py</code></summary>

```python
"""Thread-pool.

Threads run many tasks at once inside one program.

Run me:
    python 805-thread-pool/lesson_805_thread_pool.py
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
pytest 805-thread-pool
```

## 4. Open the notebook

```bash
jupyter notebook 805-thread-pool/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `thread` | A helper that runs at the same time as the program |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 804-threading](../804-threading/) · [Next: 806-thread-safety →](../806-thread-safety/)
