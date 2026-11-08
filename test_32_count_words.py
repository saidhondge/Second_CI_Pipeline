
import importlib

module = importlib.import_module("32_count_words")


def test_normal_sentence():
    assert module.count_words("Python is easy to learn") == 5


def test_single_word():
    assert module.count_words("Python") == 1


def test_empty_sentence():
    assert module.count_words("") == 0


def test_multiple_spaces():
    assert module.count_words("Python   is   easy") == 3


def test_sentence_with_punctuation():
    assert module.count_words("Hello, world! How are you?") == 5


def test_only_spaces():
    assert module.count_words("     ") == 0
