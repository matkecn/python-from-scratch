# 157 · Name-resolution

Placeholder for **Name-resolution**. A later phase replaces this with a full lesson.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 157-name-resolution/lesson_157_name_resolution.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_157_name_resolution.py</code></summary>

```python
"""Name-resolution.

Placeholder for **Name-resolution**. A later phase replaces this with a full lesson.

Run me:
    python 157-name-resolution/lesson_157_name_resolution.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"name resolution"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Name-resolution" for step in (1, 2, 3))


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
pytest 157-name-resolution
```

## 4. Open the notebook

```bash
jupyter notebook 157-name-resolution/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 156-builtins-scope](../156-builtins-scope/) · [Next: 158-shadowing →](../158-shadowing/)
