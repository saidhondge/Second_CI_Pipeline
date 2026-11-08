
import importlib

module = importlib.import_module("31_pangram")


def test_pangram_true():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False


def test_uppercase_pangram():
    assert module.is_pangram(
        "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    ) is True


def test_empty_string():
    assert module.is_pangram("") is False


def test_numbers_and_symbols():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog 123!"
    ) is True
