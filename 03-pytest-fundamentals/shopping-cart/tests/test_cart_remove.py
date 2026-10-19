import pytest


def test_remove_one_item_from_cart(full_cart, inventory):
    full_cart.remove("Berkin")
    assert full_cart.item_count() == 2
    assert full_cart.total() == pytest.approx(3000)
    assert inventory.get("Berkin").stock == 3


@pytest.mark.xfail(
    strict=True,
    reason="BUG-02: removing a product that is not in the cart fails silently "
    "instead of raising ValueError",
)
def test_remove_item_not_in_cart(full_cart, inventory):
    with pytest.raises(ValueError, match="product not in cart"):
        full_cart.remove("Port")
    assert full_cart.item_count() == 3
    assert inventory.get("Port").stock == 3


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="BUG-03: the coupon discount is not recalculated after removing "
    "a product, it stays based on the old total",
)
def test_remove_item_from_cart_with_active_coupon(full_cart, inventory):
    full_cart.apply_coupon("SAVE10")
    full_cart.remove("Dior")
    assert full_cart.total() == pytest.approx(3150)
    assert full_cart.item_count() == 2
    assert inventory.get("Dior").stock == 4
