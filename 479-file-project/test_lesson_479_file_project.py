"""Tests for File-project."""

from lesson_479_file_project import save_lines, read_lines


def test_round_trip(tmp_path) -> None:
    """The promise of lesson 'File-project' still holds."""
    assert save_lines(["one"], str(tmp_path / "demo.txt")) == 1 and read_lines(str(tmp_path / "demo.txt")) == ["one"]
