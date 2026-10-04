# 586 · Cli-subcommands

Placeholder for **Cli-subcommands**. A later phase replaces this with a full lesson.

**Section** Command line tools and logging · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 586-cli-subcommands/lesson_586_cli_subcommands.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_586_cli_subcommands.py</code></summary>

```python
"""Cli-subcommands.

Placeholder for **Cli-subcommands**. A later phase replaces this with a full lesson.

Run me:
    python 586-cli-subcommands/lesson_586_cli_subcommands.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"cli subcommands"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Cli-subcommands" for step in (1, 2, 3))


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
pytest 586-cli-subcommands
```

## 4. Open the notebook

```bash
jupyter notebook 586-cli-subcommands/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 585-cli-help](../585-cli-help/) · [Next: 587-cli-validation →](../587-cli-validation/)
