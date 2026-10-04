# 872 · Ast-transformations

Placeholder for **Ast-transformations**. A later phase replaces this with a full lesson.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 872-ast-transformations/lesson_872_ast_transformations.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_872_ast_transformations.py</code></summary>

```python
"""Ast-transformations.

Placeholder for **Ast-transformations**. A later phase replaces this with a full lesson.

Run me:
    python 872-ast-transformations/lesson_872_ast_transformations.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"ast transformations"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Ast-transformations" for step in (1, 2, 3))


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
pytest 872-ast-transformations
```

## 4. Open the notebook

```bash
jupyter notebook 872-ast-transformations/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`ast` module docs](https://docs.python.org/3/library/ast.html)

---

[← 871-ast-parsing](../871-ast-parsing/) · [Next: 873-ast-generation →](../873-ast-generation/)
