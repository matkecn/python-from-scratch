# 543 · Operator

`operator` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `operator` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 543-operator/lesson_543_operator.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_543_operator.py</code></summary>

```python
"""Operator.

`operator` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 543-operator/lesson_543_operator.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import operator

    return getattr(operator, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names operator offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import operator

    return sorted(item for item in dir(operator) if not item.startswith("_"))


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
pytest 543-operator
```

## 4. Open the notebook

```bash
jupyter notebook 543-operator/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `operator` | A standard library module for operator |

## Your turn

1. Open the REPL, `import operator`, then call `dir(operator)`.

## Read more

- [`operator` module docs](https://docs.python.org/3/library/operator.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 542-itertools](../542-itertools/) · [Next: 544-copy →](../544-copy/)
