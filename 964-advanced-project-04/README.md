# 964 · Advanced-project-04

Placeholder for **Advanced-project-04**. A later phase replaces this with a full lesson.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 964-advanced-project-04/lesson_964_advanced_project_04.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_964_advanced_project_04.py</code></summary>

```python
"""Advanced-project-04.

Placeholder for **Advanced-project-04**. A later phase replaces this with a full lesson.

Run me:
    python 964-advanced-project-04/lesson_964_advanced_project_04.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"advanced project 04"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Advanced-project-04" for step in (1, 2, 3))


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
pytest 964-advanced-project-04
```

## 4. Open the notebook

```bash
jupyter notebook 964-advanced-project-04/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 963-advanced-project-03](../963-advanced-project-03/) · [Next: 965-advanced-project-05 →](../965-advanced-project-05/)
