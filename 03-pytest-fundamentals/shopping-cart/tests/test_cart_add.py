import pytest


@pytest.mark.parametrize(
    "qty",
    [
        pytest.param(1, id="add-one"),
        pytest.param(4, id="add-whole-inventory"),
    ],
)
def test_add_items_to_cart(qty, empty_cart, inventory):
    empty_cart.add(inventory.get("Dior"), qty)
    assert empty_cart.item_count() == qty


def test_adding_product_already_in_cart(empty_cart, inventory):
    empty_cart.add(inventory.get("Dior"), 1)
    empty_cart.add(inventory.get("Dior"), 3)
    assert empty_cart.item_count() == 4


@pytest.mark.parametrize(
    "qty",
    [
        pytest.param(0, id="add-zero"),
        pytest.param(5, id="add-whole-inventory-plus-one"),
        pytest.param(-1, id="add-negative-number"),
    ],
)
def test_invalid_adds(qty, empty_cart, inventory):
    with pytest.raises(ValueError, match="invalid quantity"):
        empty_cart.add(inventory.get("Dior"), qty)
