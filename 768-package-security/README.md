# 768 · Package-security

Placeholder for **Package-security**. A later phase replaces this with a full lesson.

**Section** Packaging, style, CI and documentation · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 768-package-security/lesson_768_package_security.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_768_package_security.py</code></summary>

```python
"""Package-security.

Placeholder for **Package-security**. A later phase replaces this with a full lesson.

Run me:
    python 768-package-security/lesson_768_package_security.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"package security"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Package-security" for step in (1, 2, 3))


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
pytest 768-package-security
```

## 4. Open the notebook

```bash
jupyter notebook 768-package-security/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 767-dependency-resolution](../767-dependency-resolution/) · [Next: 769-package-project-advanced →](../769-package-project-advanced/)
