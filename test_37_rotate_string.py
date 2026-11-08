import importlib

module = importlib.import_module("37_rotate_string")
rotate_string = module.rotate_string


def test_normal_rotation():
    assert rotate_string("abcdef", 2) == "efabcd"


def test_rotate_by_one():
    assert rotate_string("hello", 1) == "ohell"


def test_rotate_by_zero():
    assert rotate_string("hello", 0) == "hello"


def test_rotate_by_full_length():
    assert rotate_string("hello", 5) == "hello"


def test_rotate_more_than_length():
    assert rotate_string("hello", 7) == "lohel"


def test_empty_string():
    assert rotate_string("", 3) == ""


def test_single_character():
    assert rotate_string("a", 5) == "a"


def test_rotation_of_long_string():
    assert rotate_string("python", 3) == "honpyt"