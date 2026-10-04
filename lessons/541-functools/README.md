# 541 · Functools

`functools` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `functools` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 541-functools/lesson_541_functools.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_541_functools.py</code></summary>

```python
"""Functools.

`functools` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 541-functools/lesson_541_functools.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import functools

    return getattr(functools, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names functools offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import functools

    return sorted(item for item in dir(functools) if not item.startswith("_"))


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
pytest 541-functools
```

## 4. Open the notebook

```bash
jupyter notebook 541-functools/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `functools` | A standard library module for functools |

## Your turn

1. Open the REPL, `import functools`, then call `dir(functools)`.

## Read more

- [`functools` module docs](https://docs.python.org/3/library/functools.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 540-collections-abc](../540-collections-abc/) · [Next: 542-itertools →](../542-itertools/)
