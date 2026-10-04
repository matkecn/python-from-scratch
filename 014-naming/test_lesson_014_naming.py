"""Tests for Naming."""

from lesson_014_naming import hides_a_builtin, is_valid_name, to_snake_case, total_price


def test_snake_case_from_words() -> None:
    """Spaces become underscores."""
    assert to_snake_case("Total Price") == "total_price"


def test_snake_case_from_dashes() -> None:
    """Dashes become underscores too."""
    assert to_snake_case("total-price") == "total_price"


def test_valid_names() -> None:
    """Lowercase words joined by underscores are fine."""
    assert is_valid_name("total_price") is True


def test_bad_names() -> None:
    """Names cannot start with a digit or be a keyword."""
    assert is_valid_name("2fast") is False
    assert is_valid_name("class") is False


def test_private_names_are_rejected() -> None:
    """A leading underscore is a private convention, not a normal name."""
    assert is_valid_name("_hidden") is False


def test_spots_hidden_builtins() -> None:
    """Using `list` as a variable would hide the real one."""
    assert hides_a_builtin("list") is True
    assert hides_a_builtin("total_price") is False


def test_price_includes_tax() -> None:
    """Two items at ten each plus twenty percent tax."""
    assert total_price(10.0, 2) == 24.0
