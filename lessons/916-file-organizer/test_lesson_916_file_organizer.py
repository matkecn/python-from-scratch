"""Tests for File-organizer."""

from lesson_916_file_organizer import save_lines, read_lines


def test_round_trip(tmp_path) -> None:
    """The promise of lesson 'File-organizer' still holds."""
    assert save_lines(["one"], str(tmp_path / "demo.txt")) == 1 and read_lines(str(tmp_path / "demo.txt")) == ["one"]
