# 800 · Open-source-project

Placeholder for **Open-source-project**. A later phase replaces this with a full lesson.

**Section** Packaging, style, CI and documentation · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 800-open-source-project/lesson_800_open_source_project.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_800_open_source_project.py</code></summary>

```python
"""Open-source-project.

Placeholder for **Open-source-project**. A later phase replaces this with a full lesson.

Run me:
    python 800-open-source-project/lesson_800_open_source_project.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"open source project"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Open-source-project" for step in (1, 2, 3))


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
pytest 800-open-source-project
```

## 4. Open the notebook

```bash
jupyter notebook 800-open-source-project/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 799-versioning](../799-versioning/) · [Next: 801-concurrency →](../801-concurrency/)
