import pytest


@pytest.mark.parametrize(
    "product, qty, coupon, expected",
    [
        pytest.param("Pilot", 4, "SAVE10", 180, id="SAVE10-200"),
        pytest.param("Port", 1, "SAVE50", 100.5, id="SAVE50-201"),
    ],
)
def test_valid_coupon(product, qty, coupon, expected, inventory, empty_cart):
    empty_cart.add(inventory.get(product), qty)
    empty_cart.apply_coupon(coupon)
    assert empty_cart.total() == pytest.approx(expected)


@pytest.mark.parametrize(
    "product, qty, coupon, expected_error",
    [
        pytest.param(
            "Pilot",
            4,
            "SAVE50",
            "cart total too low",
            id="SAVE50-200",
            marks=pytest.mark.xfail(
                strict=True,
                reason="BUG-01: SAVE50 is accepted on a total of exactly 200, "
                "but the spec requires a total above 200",
            ),
        ),
        pytest.param("Dior", 1, "SAVE70", "unknown coupon", id="nonexisting-coupon"),
    ],
)
def test_invalid_coupon(product, qty, coupon, expected_error, inventory, empty_cart):
    empty_cart.add(inventory.get(product), qty)
    with pytest.raises(ValueError, match=expected_error):
        empty_cart.apply_coupon(coupon)
