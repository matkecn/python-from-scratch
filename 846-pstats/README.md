# 846 · Pstats

`pstats` is a standard library module. This lesson shows how to look inside one.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `pstats` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 846-pstats/lesson_846_pstats.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_846_pstats.py</code></summary>

```python
"""Pstats.

`pstats` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 846-pstats/lesson_846_pstats.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import pstats

    return getattr(pstats, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names pstats offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import pstats

    return sorted(item for item in dir(pstats) if not item.startswith("_"))


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
pytest 846-pstats
```

## 4. Open the notebook

```bash
jupyter notebook 846-pstats/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `pstats` | A standard library module for pstats |

## Your turn

1. Open the REPL, `import pstats`, then call `dir(pstats)`.

## Read more

- [`pstats` module docs](https://docs.python.org/3/library/pstats.html)

---

[← 845-profile](../845-profile/) · [Next: 847-line-profiler →](../847-line-profiler/)
