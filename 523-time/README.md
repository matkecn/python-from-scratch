# 523 · Time

`time` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `time` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 523-time/lesson_523_time.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_523_time.py</code></summary>

```python
"""Time.

`time` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 523-time/lesson_523_time.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import time

    return getattr(time, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names time offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import time

    return sorted(item for item in dir(time) if not item.startswith("_"))


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
pytest 523-time
```

## 4. Open the notebook

```bash
jupyter notebook 523-time/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `time` | A standard library module for time |

## Your turn

1. Open the REPL, `import time`, then call `dir(time)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 522-date](../522-date/) · [Next: 524-timedelta →](../524-timedelta/)
