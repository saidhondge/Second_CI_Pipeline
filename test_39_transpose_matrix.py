import importlib

module = importlib.import_module("39_transpose_matrix")
transpose_matrix = module.transpose_matrix


def test_normal_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_square_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [
        [1, 3],
        [2, 4]
    ]


def test_single_row():
    assert transpose_matrix([[1, 2, 3]]) == [
        [1],
        [2],
        [3]
    ]


def test_single_column():
    assert transpose_matrix([[1], [2], [3]]) == [
        [1, 2, 3]
    ]


def test_empty_matrix():
    assert transpose_matrix([]) == []


def test_single_element():
    assert transpose_matrix([[5]]) == [[5]]


def test_negative_numbers():
    assert transpose_matrix([[-1, -2], [-3, -4]]) == [
        [-1, -3],
        [-2, -4]
    ]