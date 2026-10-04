# 494 · Tomllib

`tomllib` is a standard library module. This lesson shows how to look inside one.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `tomllib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 494-tomllib/lesson_494_tomllib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_494_tomllib.py</code></summary>

```python
"""Tomllib.

`tomllib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 494-tomllib/lesson_494_tomllib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import tomllib

    return getattr(tomllib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names tomllib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import tomllib

    return sorted(item for item in dir(tomllib) if not item.startswith("_"))


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
pytest 494-tomllib
```

## 4. Open the notebook

```bash
jupyter notebook 494-tomllib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `tomllib` | A standard library module for tomllib |

## Your turn

1. Open the REPL, `import tomllib`, then call `dir(tomllib)`.

## Read more

- [`tomllib` module docs](https://docs.python.org/3/library/tomllib.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 493-configparser](../493-configparser/) · [Next: 495-xml →](../495-xml/)
