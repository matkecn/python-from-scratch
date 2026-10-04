# 382 · Dataclass-fields

A dataclass writes the boring parts of a class for you.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- `@dataclass` builds `__init__` for you
- Every field needs a type
- `frozen=True` stops changes

## 1. Run the example

```bash
python 382-dataclass-fields/lesson_382_dataclass_fields.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_382_dataclass_fields.py</code></summary>

```python
"""Dataclass-fields.

A dataclass writes the boring parts of a class for you.

Run me:
    python 382-dataclass-fields/lesson_382_dataclass_fields.py
"""

from __future__ import annotations


from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """A point on a grid."""

    x: int
    y: int

    def distance_from_origin(self) -> float:
        """Return how far the point is from ``0, 0``.

        Returns:
            The distance, as a float.
        """
        return (self.x**2 + self.y**2) ** 0.5


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    point = Point(3, 4)
    print(point)
    print(round(point.distance_from_origin(), 2))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 382-dataclass-fields
```

## 4. Open the notebook

```bash
jupyter notebook 382-dataclass-fields/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `dataclass` | A class that generates its own `__init__` |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 381-dataclasses](../381-dataclasses/) · [Next: 383-default-factory →](../383-default-factory/)
