# 530 · Calendar

`calendar` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `calendar` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 530-calendar/lesson_530_calendar.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_530_calendar.py</code></summary>

```python
"""Calendar.

`calendar` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 530-calendar/lesson_530_calendar.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import calendar

    return getattr(calendar, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names calendar offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import calendar

    return sorted(item for item in dir(calendar) if not item.startswith("_"))


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
pytest 530-calendar
```

## 4. Open the notebook

```bash
jupyter notebook 530-calendar/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `calendar` | A standard library module for calendar |

## Your turn

1. Open the REPL, `import calendar`, then call `dir(calendar)`.

## Read more

- [`calendar` module docs](https://docs.python.org/3/library/calendar.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 529-timestamps](../529-timestamps/) · [Next: 531-collections →](../531-collections/)
