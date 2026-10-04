# 877 · Dynamic-code

Placeholder for **Dynamic-code**. A later phase replaces this with a full lesson.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 877-dynamic-code/lesson_877_dynamic_code.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_877_dynamic_code.py</code></summary>

```python
"""Dynamic-code.

Placeholder for **Dynamic-code**. A later phase replaces this with a full lesson.

Run me:
    python 877-dynamic-code/lesson_877_dynamic_code.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"dynamic code"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Dynamic-code" for step in (1, 2, 3))


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
pytest 877-dynamic-code
```

## 4. Open the notebook

```bash
jupyter notebook 877-dynamic-code/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 876-eval](../876-eval/) · [Next: 878-code-generation →](../878-code-generation/)
