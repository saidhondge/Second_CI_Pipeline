import importlib

module = importlib.import_module("36_most_frequent")


def test_single_winner():
    assert module.most_frequent([1, 3, 2, 3, 1, 3]) == 3


def test_strings():
    assert module.most_frequent(["a", "b", "a"]) == "a"


def test_tie_returns_first():
    assert module.most_frequent([1, 2, 2, 1]) == 1


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None