# 512 · Cmath

`cmath` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `cmath` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 512-cmath/lesson_512_cmath.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_512_cmath.py</code></summary>

```python
"""Cmath.

`cmath` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 512-cmath/lesson_512_cmath.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import cmath

    return getattr(cmath, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names cmath offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import cmath

    return sorted(item for item in dir(cmath) if not item.startswith("_"))


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
pytest 512-cmath
```

## 4. Open the notebook

```bash
jupyter notebook 512-cmath/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `cmath` | A standard library module for cmath |

## Your turn

1. Open the REPL, `import cmath`, then call `dir(cmath)`.

## Read more

- [`cmath` module docs](https://docs.python.org/3/library/cmath.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 511-math](../511-math/) · [Next: 513-decimal →](../513-decimal/)
