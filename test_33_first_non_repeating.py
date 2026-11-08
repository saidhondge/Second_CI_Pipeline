
import importlib

module = importlib.import_module("33_first_non_repeating")
first_non_repeating_char = module.first_non_repeating_char


def test_normal_string():
    assert first_non_repeating_char("swiss") == "w"


def test_first_character_is_unique():
    assert first_non_repeating_char("python") == "p"


def test_repeated_characters():
    assert first_non_repeating_char("aabbc") == "c"


def test_all_characters_repeated():
    assert first_non_repeating_char("aabbcc") == ""


def test_empty_string():
    assert first_non_repeating_char("") == ""


def test_single_character():
    assert first_non_repeating_char("a") == "a"
