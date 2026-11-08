
import importlib

module = importlib.import_module("35_move_zeros")
move_zeros = module.move_zeros


def test_zeros_at_beginning():
    assert move_zeros([0, 1, 2, 3]) == [1, 2, 3, 0]


def test_zeros_in_middle():
    assert move_zeros([1, 0, 2, 0, 3]) == [1, 2, 3, 0, 0]


def test_all_zeros():
    assert move_zeros([0, 0, 0]) == [0, 0, 0]


def test_no_zeros():
    assert move_zeros([1, 2, 3]) == [1, 2, 3]


def test_empty_list():
    assert move_zeros([]) == []


def test_original_list_unchanged():
    numbers = [0, 1, 0, 2]
    move_zeros(numbers)
    assert numbers == [0, 1, 0, 2]
