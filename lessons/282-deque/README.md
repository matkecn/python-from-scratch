# 282 · Deque

Placeholder for **Deque**. A later phase replaces this with a full lesson.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 282-deque/lesson_282_deque.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_282_deque.py</code></summary>

```python
"""Deque.

Placeholder for **Deque**. A later phase replaces this with a full lesson.

Run me:
    python 282-deque/lesson_282_deque.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"deque"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Deque" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 282-deque
```

## 4. Open the notebook

```bash
jupyter notebook 282-deque/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 281-collections](../281-collections/) · [Next: 283-namedtuple →](../283-namedtuple/)
