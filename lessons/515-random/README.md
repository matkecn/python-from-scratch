# 515 · Random

`random` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `random` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 515-random/lesson_515_random.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_515_random.py</code></summary>

```python
"""Random.

`random` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 515-random/lesson_515_random.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import random

    return getattr(random, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names random offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import random

    return sorted(item for item in dir(random) if not item.startswith("_"))


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
pytest 515-random
```

## 4. Open the notebook

```bash
jupyter notebook 515-random/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `random` | A standard library module for random |

## Your turn

1. Open the REPL, `import random`, then call `dir(random)`.

## Read more

- [`random` module docs](https://docs.python.org/3/library/random.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 514-fractions](../514-fractions/) · [Next: 516-secrets →](../516-secrets/)
