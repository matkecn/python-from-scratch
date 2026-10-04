"""Rebuild the notebook for one lesson folder.

Usage::

    python tools/notebook.py                    # every lesson
    python tools/notebook.py 013-variables      # one lesson
    python tools/notebook.py 000-welcome        # a folder outside the numbering

The notebook is always built from the example module, so the two can never
drift apart.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import templates
from lesson_model import Lesson

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = sorted(path for path in ROOT.iterdir() if path.is_dir() and path.name[:3].isdigit())


def topic_for(folder: Path) -> object:
    """Return a small stand in for a course topic.

    Args:
        folder: The lesson folder to describe.

    Returns:
        An object with the attributes the renderers need.
    """
    number_text, _, slug = folder.name.partition("-")
    return type(
        "FolderTopic",
        (),
        {
            "number": int(number_text),
            "slug": slug,
            "title": slug.replace("-", " ").capitalize(),
            "section": "getting-started" if number_text == "000" else "meta",
            "folder": folder.name,
            "module": next(path.stem for path in folder.glob("lesson_*.py")),
        },
    )()


def lesson_for(folder: Path) -> Lesson:
    """Read a lesson out of the files already in a folder.

    Args:
        folder: The lesson folder to read.

    Returns:
        A lesson whose source is the example module on disk.
    """
    module = topic_for(folder).module
    source = (folder / f"{module}.py").read_text(encoding="utf-8")
    test_path = next(iter(sorted(folder.glob("test_*.py"))), None)
    tests = test_path.read_text(encoding="utf-8") if test_path else ""
    docstring = ast_docstring(source)
    return Lesson(blurb=docstring, points=(), source=source, tests=tests)


def ast_docstring(source: str) -> str:
    """Return the first line of a module docstring, without the title.

    Args:
        source: Python source text.

    Returns:
        A one line summary, or an empty string.
    """
    import ast

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ""
    docstring = ast.get_docstring(tree) or ""
    lines = [line for line in docstring.splitlines() if line.strip()]
    return lines[1].strip() if len(lines) > 1 else ""


def main(argv: list[str]) -> int:
    """Rebuild notebooks and print how many were written.

    Args:
        argv: Command line arguments.

    Returns:
        The process exit code.
    """
    wanted = argv[1:]
    folders = [ROOT / name for name in wanted] if wanted else FOLDERS
    written = 0
    for folder in folders:
        if not folder.is_dir():
            print(f"no such folder: {folder}")
            return 1
        lesson = lesson_for(folder)
        before = (folder / "lesson.ipynb").read_text(encoding="utf-8") if (folder / "lesson.ipynb").exists() else ""
        after = templates.render_notebook(topic_for(folder), lesson, folder.name, folder.name)
        if after != before:
            (folder / "lesson.ipynb").write_text(after, encoding="utf-8")
            written += 1
    print(f"notebooks written: {written} of {len(folders)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
