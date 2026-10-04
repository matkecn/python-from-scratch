# 548 · Re

`re` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `re` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 548-re/lesson_548_re.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_548_re.py</code></summary>

```python
"""Re.

`re` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 548-re/lesson_548_re.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import re

    return getattr(re, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names re offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import re

    return sorted(item for item in dir(re) if not item.startswith("_"))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(module_path())
    print(len(public_names()), 'public names')


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 548-re
```

## 4. Open the notebook

```bash
jupyter notebook 548-re/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `re` | A standard library module for re |

## Your turn

1. Open the REPL, `import re`, then call `dir(re)`.

## Read more

- [`re` module docs](https://docs.python.org/3/library/re.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 547-string](../547-string/) · [Next: 549-difflib →](../549-difflib/)
