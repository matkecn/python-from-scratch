# 495 · Xml

`xml` is a standard library module. This lesson shows how to look inside one.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `xml` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 495-xml/lesson_495_xml.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_495_xml.py</code></summary>

```python
"""Xml.

`xml` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 495-xml/lesson_495_xml.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import xml

    return getattr(xml, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names xml offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import xml

    return sorted(item for item in dir(xml) if not item.startswith("_"))


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
pytest 495-xml
```

## 4. Open the notebook

```bash
jupyter notebook 495-xml/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `xml` | A standard library module for xml |

## Your turn

1. Open the REPL, `import xml`, then call `dir(xml)`.

## Read more

- [`xml` module docs](https://docs.python.org/3/library/xml.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 494-tomllib](../494-tomllib/) · [Next: 496-xml-etree →](../496-xml-etree/)
