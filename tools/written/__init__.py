"""Hand written lessons, keyed by lesson number.

Every module in this package exposes ``LESSONS``: a dictionary that maps a
lesson number from ``structure.a`` to a :class:`~tools.lesson_model.Lesson`.
Those lessons win over anything :mod:`tools.synth` generates.
"""

from __future__ import annotations

from importlib import import_module
from pathlib import Path

from lesson_model import Lesson

HANDWRITTEN: dict[int, Lesson] = {}

for _path in sorted(Path(__file__).resolve().parent.glob("s[0-9][0-9][0-9]_*.py")):
    _module = import_module(f"{__name__}.{_path.stem}")
    for _number, _lesson in getattr(_module, "LESSONS", {}).items():
        HANDWRITTEN[_number] = _lesson

__all__ = ["HANDWRITTEN"]
