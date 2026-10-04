# 517 · Statistics

`statistics` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `statistics` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 517-statistics/lesson_517_statistics.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_517_statistics.py</code></summary>

```python
"""Statistics.

`statistics` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 517-statistics/lesson_517_statistics.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import statistics

    return getattr(statistics, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names statistics offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import statistics

    return sorted(item for item in dir(statistics) if not item.startswith("_"))


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
pytest 517-statistics
```

## 4. Open the notebook

```bash
jupyter notebook 517-statistics/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `statistics` | A standard library module for statistics |

## Your turn

1. Open the REPL, `import statistics`, then call `dir(statistics)`.

## Read more

- [`statistics` module docs](https://docs.python.org/3/library/statistics.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 516-secrets](../516-secrets/) · [Next: 518-numbers →](../518-numbers/)
