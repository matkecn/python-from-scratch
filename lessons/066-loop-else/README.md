# 066 · Loop-else

Placeholder for **Loop-else**. A later phase replaces this with a full lesson.

**Section** Conditionals and loops · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 066-loop-else/lesson_066_loop_else.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_066_loop_else.py</code></summary>

```python
"""Loop-else.

Placeholder for **Loop-else**. A later phase replaces this with a full lesson.

Run me:
    python 066-loop-else/lesson_066_loop_else.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"loop else"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Loop-else" for step in (1, 2, 3))


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
pytest 066-loop-else
```

## 4. Open the notebook

```bash
jupyter notebook 066-loop-else/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/controlflow.html)

---

[← 065-pass](../065-pass/) · [Next: 067-nested-loops →](../067-nested-loops/)
