# 481 · Json

JSON is a plain text way to store lists and dictionaries.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- `json.loads` reads text
- `json.dumps` writes text
- Keys have to be text

## 1. Run the example

```bash
python 481-json/lesson_481_json.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_481_json.py</code></summary>

```python
"""Json.

JSON is a plain text way to store lists and dictionaries.

Run me:
    python 481-json/lesson_481_json.py
"""

from __future__ import annotations


import json


def to_json(data: dict) -> str:
    """Turn a dictionary into JSON text.

    Args:
        data: The data to store.

    Returns:
        The data as JSON.
    """
    return json.dumps(data, sort_keys=True)


def from_json(text: str) -> dict:
    """Read JSON text back into a dictionary.

    Args:
        text: The JSON text.

    Returns:
        The data inside.

    Raises:
        ValueError: If the text is not valid JSON.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"not valid JSON: {text!r}") from error


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    text = to_json({"name": "Ada", "age": 36})
    print(text)
    print(from_json(text))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 481-json
```

## 4. Open the notebook

```bash
jupyter notebook 481-json/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `JSON` | A plain text format for lists and dictionaries |

## Read more

- [`json` module docs](https://docs.python.org/3/library/json.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 480-pathlib-project](../480-pathlib-project/) · [Next: 482-json-load →](../482-json-load/)
