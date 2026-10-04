# 345 · Dynamic programming

Placeholder for **Dynamic programming**. A later phase replaces this with a full lesson.

**Section** Decorators, context managers, descriptors and introspection · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 345-dynamic-programming/lesson_345_dynamic_programming.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_345_dynamic_programming.py</code></summary>

```python
"""Dynamic programming.

Placeholder for **Dynamic programming**. A later phase replaces this with a full lesson.

Run me:
    python 345-dynamic-programming/lesson_345_dynamic_programming.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"dynamic programming"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Dynamic programming" for step in (1, 2, 3))


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
pytest 345-dynamic-programming
```

## 4. Open the notebook

```bash
jupyter notebook 345-dynamic-programming/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 344-class-descriptors](../344-class-descriptors/) · [Next: 346-introspection →](../346-introspection/)
