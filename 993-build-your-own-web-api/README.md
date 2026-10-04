# 993 · Build-your-own-web-api

Placeholder for **Build-your-own-web-api**. A later phase replaces this with a full lesson.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 993-build-your-own-web-api/lesson_993_build_your_own_web_api.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_993_build_your_own_web_api.py</code></summary>

```python
"""Build-your-own-web-api.

Placeholder for **Build-your-own-web-api**. A later phase replaces this with a full lesson.

Run me:
    python 993-build-your-own-web-api/lesson_993_build_your_own_web_api.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"build your own web api"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Build-your-own-web-api" for step in (1, 2, 3))


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
pytest 993-build-your-own-web-api
```

## 4. Open the notebook

```bash
jupyter notebook 993-build-your-own-web-api/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 992-build-your-own-cli](../992-build-your-own-cli/) · [Next: 994-build-your-own-database-layer →](../994-build-your-own-database-layer/)
