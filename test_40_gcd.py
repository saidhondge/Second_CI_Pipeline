import importlib

module = importlib.import_module("40_gcd")
gcd = module.gcd


def test_normal_numbers():
    assert gcd(48, 18) == 6


def test_coprime_numbers():
    assert gcd(7, 13) == 1


def test_first_number_zero():
    assert gcd(0, 5) == 5


def test_second_number_zero():
    assert gcd(10, 0) == 10


def test_both_numbers_zero():
    assert gcd(0, 0) == 0


def test_negative_numbers():
    assert gcd(-48, -18) == 6


def test_equal_numbers():
    assert gcd(12, 12) == 12


def test_one_number_is_multiple():
    assert gcd(20, 5) == 5