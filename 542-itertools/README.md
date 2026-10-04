# 542 · Itertools

`itertools` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `itertools` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 542-itertools/lesson_542_itertools.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_542_itertools.py</code></summary>

```python
"""Itertools.

`itertools` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 542-itertools/lesson_542_itertools.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import itertools

    return getattr(itertools, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names itertools offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import itertools

    return sorted(item for item in dir(itertools) if not item.startswith("_"))


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
pytest 542-itertools
```

## 4. Open the notebook

```bash
jupyter notebook 542-itertools/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `itertools` | A standard library module for itertools |

## Your turn

1. Open the REPL, `import itertools`, then call `dir(itertools)`.

## Read more

- [`itertools` module docs](https://docs.python.org/3/library/itertools.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 541-functools](../541-functools/) · [Next: 543-operator →](../543-operator/)
