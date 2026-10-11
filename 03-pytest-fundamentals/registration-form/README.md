# Registration Form - Unit Tests

Unit test suite for a user registration module: username rules, age
validation and registration fee calculation.

## What is tested

- **Username validation:** length boundaries (2/3/15/16), allowed characters
  (letters, digits, underscore), invalid character classes (non-English
  letters, space, special characters), leading digit
- **Age validation:** boundaries on both sides of the valid range (12/13,
  120/121), wrong input types (float, string) and the exact error messages
- **Fee calculation:** regular price, student discount, senior discount
  boundary (64/65), and the "discounts do not stack" rule

All expected results come from the specification in the module docstring,
not from the implementation.

## Techniques

Boundary value analysis, equivalence partitioning, negative testing,
`pytest.raises` with message matching, `pytest.approx` for float results,
`xfail(strict=True)` for tracking open bugs.

## Bugs found

| ID | Description | Found by |
|---|---|---|
| BUG-01 | Age 13 is rejected with "age out of range", although the spec allows ages 13-120 | `test_age_min_boundary_13_is_valid` |
| BUG-02 | The senior discount (30%) is applied from age 64 instead of 65 | `test_fee_age_64_pays_full_price` |

Tests for open bugs are marked `xfail(strict=True)`, so the suite stays green
while the bugs exist and turns red as soon as one is fixed, as a reminder to
remove the marker.

## Test quality check

The suite was verified with manual mutation testing: 14 deliberate changes
to the code under test (shifted boundaries, removed checks, wrong discount
rules), each caught by at least one test.

## Run

From `03-pytest-fundamentals/`:

```
pip install -r requirements.txt
pytest -v
```
