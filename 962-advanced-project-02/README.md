# 962 · Advanced-project-02

Placeholder for **Advanced-project-02**. A later phase replaces this with a full lesson.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 962-advanced-project-02/lesson_962_advanced_project_02.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_962_advanced_project_02.py</code></summary>

```python
"""Advanced-project-02.

Placeholder for **Advanced-project-02**. A later phase replaces this with a full lesson.

Run me:
    python 962-advanced-project-02/lesson_962_advanced_project_02.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"advanced project 02"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Advanced-project-02" for step in (1, 2, 3))


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
pytest 962-advanced-project-02
```

## 4. Open the notebook

```bash
jupyter notebook 962-advanced-project-02/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 961-advanced-project-01](../961-advanced-project-01/) · [Next: 963-advanced-project-03 →](../963-advanced-project-03/)
