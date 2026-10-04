"""The data model every lesson shares.

A lesson is pure data. The renderers in :mod:`tools.templates` turn that data
into the four files a learner sees: a README, an example module, a pytest file
and a Jupyter notebook.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass

__all__ = ["Lesson", "public_names", "STATUS_WRITTEN", "STATUS_DRAFT"]

STATUS_WRITTEN = "written"
STATUS_DRAFT = "draft"


@dataclass(frozen=True)
class Lesson:
    """Everything needed to render one lesson directory.

    Attributes:
        blurb: One friendly sentence describing the lesson.
        points: Short bullets for the "What you will learn" section.
        source: Full text of the example module.
        tests: Full text of the pytest module.
        practice: Prompts used by the notebook's "Your turn" cells.
        glossary: Short term and meaning pairs for "Words to remember".
        read_more: Extra documentation links.
        status: ``"written"`` for hand written lessons, ``"draft"`` for
            generated placeholders that a later phase replaces.
    """

    blurb: str
    points: tuple[str, ...]
    source: str
    tests: str
    practice: tuple[str, ...] = ()
    glossary: tuple[tuple[str, str], ...] = ()
    read_more: tuple[str, ...] = ()
    status: str = STATUS_WRITTEN

    def names(self) -> tuple[str, ...]:
        """Return the public names a learner can call in the example module."""
        return public_names(self.source)


def public_names(source: str) -> tuple[str, ...]:
    """Return top level function and class names from Python source.

    Private names and the ``main`` entry point are skipped so generated tests
    and notebooks only import the useful things.

    Args:
        source: Python source text.

    Returns:
        Names in the order they appear.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ()
    names: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef):
            if not node.name.startswith("_") and node.name != "main":
                names.append(node.name)
    return tuple(names)
