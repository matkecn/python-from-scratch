# 493 · Configparser

`configparser` is a standard library module. This lesson shows how to look inside one.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `configparser` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 493-configparser/lesson_493_configparser.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_493_configparser.py</code></summary>

```python
"""Configparser.

`configparser` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 493-configparser/lesson_493_configparser.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import configparser

    return getattr(configparser, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names configparser offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import configparser

    return sorted(item for item in dir(configparser) if not item.startswith("_"))


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
pytest 493-configparser
```

## 4. Open the notebook

```bash
jupyter notebook 493-configparser/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `configparser` | A standard library module for configparser |

## Your turn

1. Open the REPL, `import configparser`, then call `dir(configparser)`.

## Read more

- [`configparser` module docs](https://docs.python.org/3/library/configparser.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 492-shelve](../492-shelve/) · [Next: 494-tomllib →](../494-tomllib/)
