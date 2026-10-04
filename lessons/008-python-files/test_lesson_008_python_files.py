"""Tests for Python files."""

from lesson_008_python_files import count_lines, is_python_file, read_script, write_script


def test_writes_a_file(tmp_path) -> None:
    """The file lands on disk with the lines we gave it."""
    target = str(tmp_path / "demo.py")
    assert write_script(target, ["print('hi')"]) == 1
    assert (tmp_path / "demo.py").exists()


def test_reads_it_back(tmp_path) -> None:
    """What we wrote is what we read."""
    target = str(tmp_path / "demo.py")
    write_script(target, ["one", "two", "three"])
    assert read_script(target) == ["one", "two", "three"]


def test_counts_lines(tmp_path) -> None:
    """Counting lines agrees with reading them."""
    target = str(tmp_path / "demo.py")
    write_script(target, ["a", "b"])
    assert count_lines(target) == 2


def test_recognises_python_files() -> None:
    """Only names ending in .py count."""
    assert is_python_file("game.py") is True
    assert is_python_file("game.txt") is False
