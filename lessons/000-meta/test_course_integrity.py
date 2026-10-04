"""Tests that check the course itself rather than one lesson."""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import curriculum  # noqa: E402

EXPECTED_LESSONS = 999
EXPECTED_FILES = ("README.md", "lesson.ipynb")


def lesson_folder(topic: curriculum.Topic) -> Path:
    """Return the folder that holds a lesson.

    Args:
        topic: The lesson to look for.

    Returns:
        The path of the lesson folder.
    """
    return ROOT / curriculum.lesson_dir(topic.number)


def test_there_are_999_lessons() -> None:
    """The course holds exactly 999 numbered lessons."""
    assert len(curriculum.TOPICS) == EXPECTED_LESSONS


def test_lessons_run_from_1_to_999_in_order() -> None:
    """Lesson numbers never skip and never repeat."""
    numbers = [topic.number for topic in curriculum.TOPICS]
    assert numbers == list(range(1, EXPECTED_LESSONS + 1))


def test_every_folder_name_is_unique() -> None:
    """Two lessons never share a folder name."""
    folders = [topic.folder for topic in curriculum.TOPICS]
    assert len(set(folders)) == EXPECTED_LESSONS


def test_every_module_name_is_unique_and_importable() -> None:
    """Two lessons never share a module name, and each is a valid identifier."""
    modules = [topic.module for topic in curriculum.TOPICS]
    assert len(set(modules)) == EXPECTED_LESSONS
    assert all(module.isidentifier() for module in modules)


def test_no_module_name_shadows_the_standard_library() -> None:
    """Lesson modules are prefixed, so `import copy` still means the real copy."""
    clashes = [topic.module for topic in curriculum.TOPICS if topic.module in sys.stdlib_module_names]
    assert clashes == []


def test_every_lesson_has_all_four_files() -> None:
    """Each lesson folder holds a README, an example, tests and a notebook."""
    missing: list[str] = []
    for topic in curriculum.TOPICS:
        folder = lesson_folder(topic)
        for name in (*EXPECTED_FILES, f"{topic.module}.py", f"{topic.test_module}.py"):
            if not (folder / name).exists():
                missing.append(f"{topic.folder}/{name}")
    assert missing == []


def test_every_example_module_has_a_docstring() -> None:
    """Each example module explains itself at the top."""
    without: list[str] = []
    for topic in curriculum.TOPICS:
        source = (lesson_folder(topic) / f"{topic.module}.py").read_text(encoding="utf-8")
        if ast.get_docstring(ast.parse(source)) is None:
            without.append(topic.folder)
    assert without == []


def test_every_notebook_is_valid_json() -> None:
    """Each notebook is readable by Jupyter."""
    broken: list[str] = []
    for topic in curriculum.TOPICS:
        path = lesson_folder(topic) / "lesson.ipynb"
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            broken.append(topic.folder)
            continue
        if notebook.get("nbformat") != 4 or not notebook.get("cells"):
            broken.append(topic.folder)
    assert broken == []


def test_every_readme_links_to_real_neighbours() -> None:
    """The previous and next links in a README point at folders that exist."""
    broken: list[str] = []
    topics = curriculum.TOPICS
    for index, topic in enumerate(topics):
        readme = (lesson_folder(topic) / "README.md").read_text(encoding="utf-8")
        before = "000-welcome" if index == 0 else topics[index - 1].folder
        after = topics[index + 1].folder if index + 1 < len(topics) else None
        if f"../{before}/" not in readme:
            broken.append(f"{topic.folder} is missing a link to {before}")
        if after is not None and f"../{after}/" not in readme:
            broken.append(f"{topic.folder} is missing a link to {after}")
    assert broken == []


def test_every_section_covers_a_contiguous_range() -> None:
    """Sections are in order and do not overlap."""
    ranges = [(section.start, section.end) for section in curriculum.SECTIONS]
    assert ranges == sorted(ranges)
    for (_, end), (start, _) in zip(ranges, ranges[1:], strict=False):
        assert start == end + 1
