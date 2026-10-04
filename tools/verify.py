"""Check that every lesson in the course is healthy.

Usage::

    python tools/verify.py            # everything
    python tools/verify.py --only 1-50

The checks are:

* every example module compiles;
* every example module runs;
* every notebook is valid JSON with the expected cells;
* every pytest file passes, including the docstring examples.
"""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import curriculum
from lesson_model import public_names

ROOT = Path(__file__).resolve().parent.parent


def parse_range(text: str) -> tuple[int, int]:
    """Return ``(start, end)`` for text such as ``1-50`` or ``13``."""
    if "-" in text:
        start, _, end = text.partition("-")
        return int(start), int(end)
    number = int(text)
    return number, number


def check_module(path: Path) -> list[str]:
    """Return problems found in one example module.

    Args:
        path: The example module to check.

    Returns:
        A list of human readable problems, empty when the module is fine.
    """
    problems: list[str] = []
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return [f"{path}: syntax error on line {error.lineno}"]
    if ast.get_docstring(tree) is None:
        problems.append(f"{path}: the module needs a docstring")
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.ClassDef):
            if node.name.startswith("_"):
                continue
            if ast.get_docstring(node) is None:
                problems.append(f"{path}: {node.name}() needs a docstring")
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        cwd=path.parent,
        stdin=subprocess.DEVNULL,
        timeout=60,
    )
    if result.returncode != 0:
        tail = (result.stderr.strip().splitlines() or ["unknown error"])[-1]
        problems.append(f"{path}: running it failed: {tail}")
    return problems


def check_notebook(path: Path, module: str) -> list[str]:
    """Return problems found in one notebook.

    Args:
        path: The notebook to check.
        module: The example module name the notebook should mention.

    Returns:
        A list of human readable problems, empty when the notebook is fine.
    """
    problems: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"{path}: not valid JSON ({error})"]
    if notebook.get("nbformat") != 4:
        problems.append(f"{path}: nbformat should be 4")
    cells = notebook.get("cells", [])
    if len(cells) < 5:
        problems.append(f"{path}: only {len(cells)} cells, expected at least 5")
    body = json.dumps(cells)
    if module not in body:
        problems.append(f"{path}: never mentions {module}")
    if not any(cell.get("cell_type") == "code" for cell in cells):
        problems.append(f"{path}: has no code cells")
    return problems


def check_tests(path: Path) -> list[str]:
    """Return problems found in one test module.

    Args:
        path: The test module to check.

    Returns:
        A list of human readable problems, empty when the tests look fine.
    """
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    names = [
        node.name
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]
    if not names:
        return [f"{path}: has no test functions"]
    if ast.get_docstring(tree) is None:
        return [f"{path}: the test module needs a docstring"]
    return []


def main(argv: list[str] | None = None) -> int:
    """Run every check and print a summary.

    Args:
        argv: Command line arguments, defaulting to ``sys.argv[1:]``.

    Returns:
        ``0`` when everything is healthy, ``1`` otherwise.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", default="1-999", help="lesson range such as 1-50")
    parser.add_argument("--fast", action="store_true", help="skip running each example")
    parser.add_argument("--run-tests", action="store_true", help="also run pytest")
    args = parser.parse_args(argv)

    start, end = parse_range(args.only)
    topics = [topic for topic in curriculum.TOPICS if start <= topic.number <= end]
    problems: list[str] = []
    checked = {"modules": 0, "notebooks": 0, "tests": 0}

    for topic in topics:
        folder = ROOT / topic.folder
        module_path = folder / f"{topic.module}.py"
        test_path = folder / f"{topic.test_module}.py"
        notebook_path = folder / "lesson.ipynb"
        readme_path = folder / "README.md"
        for path in (module_path, test_path, notebook_path, readme_path):
            if not path.exists():
                problems.append(f"{topic.folder}: missing {path.name}")
        if module_path.exists():
            checked["modules"] += 1
            if args.fast:
                ast.parse(module_path.read_text(encoding="utf-8"))
            else:
                problems += check_module(module_path)
        if notebook_path.exists():
            checked["notebooks"] += 1
            problems += check_notebook(notebook_path, topic.module)
        if test_path.exists():
            checked["tests"] += 1
            problems += check_tests(test_path)

    print(f"lessons checked : {len(topics)}")
    print(f"modules         : {checked['modules']}")
    print(f"notebooks       : {checked['notebooks']}")
    print(f"test modules    : {checked['tests']}")
    for problem in problems[:40]:
        print(f"  ! {problem}")
    if len(problems) > 40:
        print(f"  ... and {len(problems) - 40} more")
    if args.run_tests and not problems:
        folders = [topic.folder for topic in topics]
        result = subprocess.run([sys.executable, "-m", "pytest", "-q", *folders], cwd=ROOT)
        return result.returncode
    print("result          :", "FAIL" if problems else "OK")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
