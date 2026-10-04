# 827 · Create-task

Placeholder for **Create-task**. A later phase replaces this with a full lesson.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 827-create-task/lesson_827_create_task.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_827_create_task.py</code></summary>

```python
"""Create-task.

Placeholder for **Create-task**. A later phase replaces this with a full lesson.

Run me:
    python 827-create-task/lesson_827_create_task.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"create task"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Create-task" for step in (1, 2, 3))


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
pytest 827-create-task
```

## 4. Open the notebook

```bash
jupyter notebook 827-create-task/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 826-async-tasks](../826-async-tasks/) · [Next: 828-gather →](../828-gather/)
