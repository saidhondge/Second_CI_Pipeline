
import importlib

module = importlib.import_module("34_check_sorted")
is_sorted = module.is_sorted


def test_sorted_list():
    assert is_sorted([1, 2, 3, 4, 5]) is True


def test_unsorted_list():
    assert is_sorted([5, 2, 3, 1]) is False


def test_empty_list():
    assert is_sorted([]) is True


def test_single_element():
    assert is_sorted([10]) is True


def test_duplicate_elements():
    assert is_sorted([1, 2, 2, 3]) is True


def test_reverse_sorted_list():
    assert is_sorted([5, 4, 3, 2, 1]) is False
