# 902 · Cli-calculator

Placeholder for **Cli-calculator**. A later phase replaces this with a full lesson.

**Section** Practical Python applications · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 902-cli-calculator/lesson_902_cli_calculator.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_902_cli_calculator.py</code></summary>

```python
"""Cli-calculator.

Placeholder for **Cli-calculator**. A later phase replaces this with a full lesson.

Run me:
    python 902-cli-calculator/lesson_902_cli_calculator.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"cli calculator"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Cli-calculator" for step in (1, 2, 3))


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
pytest 902-cli-calculator
```

## 4. Open the notebook

```bash
jupyter notebook 902-cli-calculator/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 901-cli-apps](../901-cli-apps/) · [Next: 903-cli-todo →](../903-cli-todo/)
