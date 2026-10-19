# Shopping Cart - Unit Tests

Unit test suite for an online shopping cart module: adding and removing
products, stock reservation in the warehouse, and coupon discounts.

## What is tested

- **Adding products:** valid quantities (1, the whole stock), invalid
  quantities (0, stock + 1, negative) with the exact error message, and
  adding a product that is already in the cart (quantity is added, not replaced)
- **Coupons:** SAVE10, SAVE50 on both sides of the 200 ILS boundary (200/201),
  and an unknown code that looks like a real one (SAVE70)
- **Removing products:** cart count, total and warehouse stock after a removal;
  removing a product that is not in the cart (error raised, cart and stock
  unchanged); total recalculation after a removal with an active coupon

All expected results come from the specification in the module docstring,
not from the implementation.

## Techniques

Boundary value analysis, equivalence partitioning, negative testing,
side-effect checks after failed actions, `@pytest.mark.parametrize` with
readable ids, fixtures with `yield` shared through `conftest.py`, fixture
composition (`full_cart` builds on `inventory`), fixture scope for test
isolation, `pytest.approx`, `xfail(strict=True)` for tracking open bugs.

## Test isolation

The `inventory` fixture started with `scope="module"`. Tests that change the
stock leaked state into each other: one test failed when it should pass, and
another passed only because of the test that ran before it. The scope was
changed to `function`, so each test gets a clean warehouse. The full reasoning
is in [`tests/conftest.py`](tests/conftest.py).

## Bugs found

| ID | Description | Found by |
|---|---|---|
| BUG-01 | SAVE50 is accepted on a total of exactly 200, but the spec requires a total above 200 | `test_invalid_coupon[SAVE50-200]` |
| BUG-02 | Removing a product that is not in the cart fails silently instead of raising `ValueError("product not in cart")` | `test_remove_item_not_in_cart` |
| BUG-03 | After removing a product from a cart with a coupon, the discount stays based on the old total instead of being recalculated | `test_remove_item_from_cart_with_active_coupon` |

Tests for open bugs are marked `xfail(strict=True)`, so the suite stays green
while the bugs exist and turns red as soon as one is fixed, as a reminder to
remove the marker.

## Open question on the specification

The spec does not define what happens when a cart is above 200 with SAVE50
applied, and a removal brings the total below 200. Is the coupon cancelled
(full price), or does it stay and apply 50% to the new total? This case is not
tested until the expected behavior is defined.

## Test quality check

- The suite was run against a copy of the module with the three bugs fixed:
  all tests passed, confirming that each failure was caused by a real bug and
  not by a mistake in the test.
- Manual mutation testing: 7 deliberate changes to the code under test (wrong
  discount rate, missing coupon validation, stock not reserved or released,
  wrong item count, quantity ignored in the total, quantity replaced instead
  of added), each caught by at least one test.

## Run

From `03-pytest-fundamentals/`:

```
pip install -r requirements.txt
pytest shopping-cart -v
```
