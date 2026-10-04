# 511 · Math

`math` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `math` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 511-math/lesson_511_math.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_511_math.py</code></summary>

```python
"""Math.

`math` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 511-math/lesson_511_math.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import math

    return getattr(math, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names math offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import math

    return sorted(item for item in dir(math) if not item.startswith("_"))


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
pytest 511-math
```

## 4. Open the notebook

```bash
jupyter notebook 511-math/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `math` | A standard library module for math |

## Your turn

1. Open the REPL, `import math`, then call `dir(math)`.

## Read more

- [`math` module docs](https://docs.python.org/3/library/math.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 510-process-management](../510-process-management/) · [Next: 512-cmath →](../512-cmath/)
