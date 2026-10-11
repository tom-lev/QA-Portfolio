"""User registration module (system under test).

Specification:

validate_username(name)
    Returns True if the username is valid, otherwise False. A valid username:
    - is 3 to 15 characters long (inclusive),
    - contains only English letters (upper or lower case), digits and underscore (_),
    - does not start with a digit.

validate_age(age)
    - Raises ValueError("age must be a number") if age is not an int.
    - Raises ValueError("age out of range") if age is below 13 or above 120.
    - Otherwise returns True.

calculate_fee(age, is_student)
    Returns the registration fee as a float:
    - The base fee is 100.
    - Students get a 50% discount.
    - Users aged 65 and over get a 30% discount.
    - Discounts do not stack: if both apply, only the larger one is given.
"""
import re


def validate_username(name):
    if len(name) < 3 or len(name) > 15:
        return False
    if name[0].isdigit():
        return False
    return re.fullmatch(r"[A-Za-z0-9_]+", name) is not None


def validate_age(age):
    if not isinstance(age, int):
        raise ValueError("age must be a number")
    if age <= 13 or age > 120:
        raise ValueError("age out of range")
    return True


def calculate_fee(age, is_student):
    base_fee = 100.0
    discount = 0.0
    if is_student:
        discount = 0.5
    if age >= 64:
        discount = max(discount, 0.3)
    return base_fee * (1 - discount)
