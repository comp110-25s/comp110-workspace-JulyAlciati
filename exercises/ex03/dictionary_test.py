"""Dictionary Test in class COMP110!"""

__author__: str = "730715920"


import pytest
from dictionary import invert
from dictionary import count
from dictionary import favorite_color
from dictionary import bin_len


def test_invert_normal() -> None:
    """Test a normal dictionary with unique values."""
    input_dict = {"a": "z", "b": "y", "c": "x"}
    expected = {"z": "a", "y": "b", "x": "c"}
    assert invert(input_dict) == expected


def test_invert_single_pair() -> None:
    """Test dictionary with only one key-value pair."""
    input_dict = {"apple": "cat"}
    expected = {"cat": "apple"}
    assert invert(input_dict) == expected


def test_invert_duplicate_value() -> None:
    """Test that a KeyError is raised when values are duplicated."""
    input_dict = {"kris": "jordan", "michael": "jordan"}
    with pytest.raises(KeyError):
        invert(input_dict)


def test_invert_empty() -> None:
    """Test inverting an empty dictionary."""
    assert invert({}) == {}


def test_invert_order_independence() -> None:
    """Test that the inversion works regardless of key order."""
    input_dict = {"x": "1", "y": "2"}
    result = invert(input_dict)
    assert result == {"1": "x", "2": "y"}


def test_count_multiple_repeats() -> None:
    """Test with multiple repeated items."""
    input_list = ["apple", "banana", "apple", "apple", "banana", "cherry"]
    expected = {"apple": 3, "banana": 2, "cherry": 1}
    assert count(input_list) == expected


def test_count_all_unique() -> None:
    """Test where all elements are unique."""
    input_list = ["red", "green", "blue"]
    expected = {"red": 1, "green": 1, "blue": 1}
    assert count(input_list) == expected


def test_count_all_same() -> None:
    """Test where all elements are the same."""
    input_list = ["yes", "yes", "yes"]
    expected = {"yes": 3}
    assert count(input_list) == expected


def test_count_empty_list() -> None:
    """Test with an empty list."""
    assert count([]) == {}


def test_count_case_sensitive() -> None:
    """Test that the function treats values with different cases as different keys."""
    input_list = ["Yes", "yes", "YES"]
    expected = {"Yes": 1, "yes": 1, "YES": 1}
    assert count(input_list) == expected


def test_favorite_color_simple() -> None:
    input_dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(input_dict) == "blue"


def test_favorite_color_tie_returns_first() -> None:
    input_dict = {"A": "red", "B": "blue", "C": "red", "D": "blue"}
    assert favorite_color(input_dict) == "red"


def test_favorite_color_all_unique() -> None:
    input_dict = {"A": "green", "B": "yellow", "C": "pink"}
    assert favorite_color(input_dict) == "green"


def test_favorite_color_empty() -> None:
    assert favorite_color({}) == ""


def test_bin_len_mixed_lengths() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_duplicates() -> None:
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty() -> None:
    assert bin_len([]) == {}


def test_bin_len_all_same_length() -> None:
    assert bin_len(["one", "two", "six"]) == {3: {"one", "two", "six"}}


def test_bin_len_varied_lengths_and_duplicates() -> None:
    input_list = ["cat", "catch", "dog", "mouse", "bat", "cat", "dog"]
    expected = {3: {"cat", "dog", "bat"}, 5: {"catch", "mouse"}}
    assert bin_len(input_list) == expected
