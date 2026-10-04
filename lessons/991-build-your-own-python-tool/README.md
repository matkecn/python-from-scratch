# 991 · Build-your-own-python-tool

Placeholder for **Build-your-own-python-tool**. A later phase replaces this with a full lesson.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 991-build-your-own-python-tool/lesson_991_build_your_own_python_tool.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_991_build_your_own_python_tool.py</code></summary>

```python
"""Build-your-own-python-tool.

Placeholder for **Build-your-own-python-tool**. A later phase replaces this with a full lesson.

Run me:
    python 991-build-your-own-python-tool/lesson_991_build_your_own_python_tool.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"build your own python tool"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Build-your-own-python-tool" for step in (1, 2, 3))


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
pytest 991-build-your-own-python-tool
```

## 4. Open the notebook

```bash
jupyter notebook 991-build-your-own-python-tool/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 990-open-source-challenges](../990-open-source-challenges/) · [Next: 992-build-your-own-cli →](../992-build-your-own-cli/)
