# 815 · Threading-project

Placeholder for **Threading-project**. A later phase replaces this with a full lesson.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 815-threading-project/lesson_815_threading_project.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_815_threading_project.py</code></summary>

```python
"""Threading-project.

Placeholder for **Threading-project**. A later phase replaces this with a full lesson.

Run me:
    python 815-threading-project/lesson_815_threading_project.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"threading project"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Threading-project" for step in (1, 2, 3))


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
pytest 815-threading-project
```

## 4. Open the notebook

```bash
jupyter notebook 815-threading-project/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`threading` module docs](https://docs.python.org/3/library/threading.html)

---

[← 814-producer-consumer](../814-producer-consumer/) · [Next: 816-multiprocessing →](../816-multiprocessing/)
