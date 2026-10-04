# 381 · Dataclasses

A dataclass writes the boring parts of a class for you.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- `@dataclass` builds `__init__` for you
- Every field needs a type
- `frozen=True` stops changes

## 1. Run the example

```bash
python 381-dataclasses/lesson_381_dataclasses.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_381_dataclasses.py</code></summary>

```python
"""Dataclasses.

A dataclass writes the boring parts of a class for you.

Run me:
    python 381-dataclasses/lesson_381_dataclasses.py
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
pytest 381-dataclasses
```

## 4. Open the notebook

```bash
jupyter notebook 381-dataclasses/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `dataclass` | A class that generates its own `__init__` |

## Read more

- [`dataclasses` module docs](https://docs.python.org/3/library/dataclasses.html)
- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 380-type-safe-project](../380-type-safe-project/) · [Next: 382-dataclass-fields →](../382-dataclass-fields/)
