# 997 · Build-your-own-orm

Placeholder for **Build-your-own-orm**. A later phase replaces this with a full lesson.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 997-build-your-own-orm/lesson_997_build_your_own_orm.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_997_build_your_own_orm.py</code></summary>

```python
"""Build-your-own-orm.

Placeholder for **Build-your-own-orm**. A later phase replaces this with a full lesson.

Run me:
    python 997-build-your-own-orm/lesson_997_build_your_own_orm.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"build your own orm"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Build-your-own-orm" for step in (1, 2, 3))


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
pytest 997-build-your-own-orm
```

## 4. Open the notebook

```bash
jupyter notebook 997-build-your-own-orm/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 996-build-your-own-package](../996-build-your-own-package/) · [Next: 998-build-your-own-interpreter →](../998-build-your-own-interpreter/)
