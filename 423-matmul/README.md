# 423 · __matmul__

Placeholder for **__matmul__**. A later phase replaces this with a full lesson.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 423-matmul/lesson_423_matmul.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_423_matmul.py</code></summary>

```python
"""__matmul__.

Placeholder for **__matmul__**. A later phase replaces this with a full lesson.

Run me:
    python 423-matmul/lesson_423_matmul.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"matmul"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. __matmul__" for step in (1, 2, 3))


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
pytest 423-matmul
```

## 4. Open the notebook

```bash
jupyter notebook 423-matmul/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 422-pow](../422-pow/) · [Next: 424-bitwise-dunders →](../424-bitwise-dunders/)
