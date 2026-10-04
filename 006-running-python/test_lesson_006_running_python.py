"""Tests for Running Python."""

from lesson_006_running_python import run_line, run_script, write_script


def test_runs_a_single_line() -> None:
    """One line of code runs and prints."""
    assert run_line("print(6 * 7)") == "42"


def test_a_written_script_runs(tmp_path) -> None:
    """A file we write ourselves can be run."""
    target = write_script(str(tmp_path / "tiny.py"))
    assert target.exists()


def test_running_a_script_prints_its_line(tmp_path) -> None:
    """The script says hello when it runs."""
    target = write_script(str(tmp_path / "tiny.py"))
    assert run_script(str(target)) == "the script ran"
