import importlib

module = importlib.import_module("38_missing_number_xor")
find_missing_number = module.find_missing_number


def test_missing_middle_number():
    assert find_missing_number([1, 2, 4, 5]) == 3


def test_missing_first_number():
    assert find_missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert find_missing_number([1, 2, 3, 4]) == 5


def test_two_numbers():
    assert find_missing_number([1]) == 2


def test_large_numbers():
    assert find_missing_number([1, 2, 3, 5, 6, 7]) == 4


def test_single_missing_number():
    assert find_missing_number([2]) == 1


def test_missing_number_from_long_list():
    assert find_missing_number([1, 2, 3, 4, 5, 6, 8, 9, 10]) == 7