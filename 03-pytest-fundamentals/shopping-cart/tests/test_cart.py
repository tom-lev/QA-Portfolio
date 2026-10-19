def test_inventory_has_all_products(inventory):
    assert inventory.get("Berkin").name == "Berkin"
    assert inventory.get("Dior").name == "Dior"
    assert inventory.get("Tesla").name == "Tesla"
    assert inventory.get("Kitchenaid").name == "Kitchenaid"
    assert inventory.get("Pilot").name == "Pilot"
    assert inventory.get("Port").name == "Port"


def test_cart_is_empty(empty_cart):
    assert empty_cart.item_count() == 0


def test_cart_is_full(full_cart):
    assert full_cart.item_count() == 3
