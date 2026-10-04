"""Tests for Text-files."""

from lesson_457_text_files import save_lines, read_lines


def test_round_trip(tmp_path) -> None:
    """The promise of lesson 'Text-files' still holds."""
    assert save_lines(["one"], str(tmp_path / "demo.txt")) == 1 and read_lines(str(tmp_path / "demo.txt")) == ["one"]
