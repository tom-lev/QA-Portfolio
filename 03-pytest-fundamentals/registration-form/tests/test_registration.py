"""Unit tests for the registration module.

Test design: boundary value analysis and equivalence partitioning,
derived from the specification in registration.py (not from the code).

Open bugs are marked xfail(strict=True): the suite stays green while the
bug exists, and the test turns red as soon as the bug is fixed, as a
reminder to remove the marker.
"""
import pytest

from registration import calculate_fee, validate_age, validate_username


# ---------- validate_username: valid ----------

def test_username_min_length_3_is_valid():
    assert validate_username("tom") is True


def test_username_max_length_15_is_valid():
    assert validate_username("TomerLevin12345") is True


def test_username_with_underscore_is_valid():
    assert validate_username("tomer_levin") is True


# ---------- validate_username: invalid ----------

def test_username_length_2_is_invalid():
    assert validate_username("to") is False


def test_username_length_16_is_invalid():
    assert validate_username("tomer_levin12345") is False


def test_username_starting_with_digit_is_invalid():
    assert validate_username("1tomer") is False


def test_username_with_non_english_letters_is_invalid():
    assert validate_username("tomerלוין") is False


def test_username_with_space_is_invalid():
    assert validate_username("tom lev") is False


def test_username_with_special_char_is_invalid():
    assert validate_username("tomer!") is False


# ---------- validate_age: valid ----------

def test_age_typical_value_is_valid():
    assert validate_age(50) is True


@pytest.mark.xfail(
    strict=True,
    raises=ValueError,
    reason="BUG-01: age 13 is rejected, but the spec allows ages 13-120",
)
def test_age_min_boundary_13_is_valid():
    assert validate_age(13) is True


def test_age_max_boundary_120_is_valid():
    assert validate_age(120) is True


# ---------- validate_age: invalid ----------

def test_age_12_is_out_of_range():
    with pytest.raises(ValueError, match="age out of range"):
        validate_age(12)


def test_age_121_is_out_of_range():
    with pytest.raises(ValueError, match="age out of range"):
        validate_age(121)


def test_age_float_is_rejected():
    with pytest.raises(ValueError, match="age must be a number"):
        validate_age(21.5)


def test_age_string_is_rejected():
    with pytest.raises(ValueError, match="age must be a number"):
        validate_age("fifty")


# ---------- calculate_fee ----------

def test_fee_regular_user_pays_full_price():
    assert calculate_fee(30, False) == pytest.approx(100)


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="BUG-02: the senior discount is applied from age 64 instead of 65",
)
def test_fee_age_64_pays_full_price():
    assert calculate_fee(64, False) == pytest.approx(100)


def test_fee_age_65_gets_senior_discount():
    assert calculate_fee(65, False) == pytest.approx(70)


def test_fee_age_70_gets_senior_discount():
    assert calculate_fee(70, False) == pytest.approx(70)


def test_fee_student_gets_student_discount():
    assert calculate_fee(30, True) == pytest.approx(50)


def test_fee_senior_student_gets_larger_discount_only():
    assert calculate_fee(70, True) == pytest.approx(50)
