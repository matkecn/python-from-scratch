"""Tests for File-copy."""

from lesson_470_file_copy import save_lines, read_lines


def test_round_trip(tmp_path) -> None:
    """The promise of lesson 'File-copy' still holds."""
    assert save_lines(["one"], str(tmp_path / "demo.txt")) == 1 and read_lines(str(tmp_path / "demo.txt")) == ["one"]
