# 869 · Ast

`ast` is a standard library module. This lesson shows how to look inside one.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `ast` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 869-ast/lesson_869_ast.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_869_ast.py</code></summary>

```python
"""Ast.

`ast` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 869-ast/lesson_869_ast.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import ast

    return getattr(ast, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names ast offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import ast

    return sorted(item for item in dir(ast) if not item.startswith("_"))


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
pytest 869-ast
```

## 4. Open the notebook

```bash
jupyter notebook 869-ast/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `ast` | A standard library module for ast |

## Your turn

1. Open the REPL, `import ast`, then call `dir(ast)`.

## Read more

- [`ast` module docs](https://docs.python.org/3/library/ast.html)

---

[← 868-module-objects](../868-module-objects/) · [Next: 870-ast-module →](../870-ast-module/)
