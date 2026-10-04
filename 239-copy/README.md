# 239 · Copy

`copy` is a standard library module. This lesson shows how to look inside one.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `copy` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 239-copy/lesson_239_copy.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_239_copy.py</code></summary>

```python
"""Copy.

`copy` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 239-copy/lesson_239_copy.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import copy

    return getattr(copy, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names copy offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import copy

    return sorted(item for item in dir(copy) if not item.startswith("_"))


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
pytest 239-copy
```

## 4. Open the notebook

```bash
jupyter notebook 239-copy/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `copy` | A standard library module for copy |

## Your turn

1. Open the REPL, `import copy`, then call `dir(copy)`.

## Read more

- [`copy` module docs](https://docs.python.org/3/library/copy.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 238-del](../238-del/) · [Next: 240-deepcopy →](../240-deepcopy/)
