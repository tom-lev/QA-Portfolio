"""Shared fixtures for the shopping cart tests.

Fixture scope decision: `inventory` started with scope="module", so it was
created once per test file and shared by all its tests. The tests were not
isolated: one test changed the stock and the next one got a "dirty"
warehouse. A test that should pass failed, and another passed by accident
(add-whole-inventory-plus-one passed only because the stock was already 0,
and failed when run alone). The scope was changed to "function", so every
test runs against a clean warehouse. The setup is cheap (no browser or DB),
so the cost of creating it per test is negligible.
"""

import pytest
from cart import Inventory, Product, Cart


@pytest.fixture(scope="function")
def inventory():
    bag = Product("Berkin", 1000, 3)
    coat = Product("Dior", 500, 4)
    car = Product("Tesla", 2500, 2)
    mixer = Product("Kitchenaid", 700, 3)
    pen = Product("Pilot", 50, 50)
    wine = Product("Port", 201, 3)

    inventory = Inventory([bag, coat, car, mixer, pen, wine])

    yield inventory

    print("\ninventory closed")


@pytest.fixture
def empty_cart(inventory):
    cart = Cart(inventory)
    yield cart


@pytest.fixture
def full_cart(inventory):
    full_cart = Cart(inventory)
    full_cart.add(inventory.get("Berkin"), 1)
    full_cart.add(inventory.get("Tesla"), 1)
    full_cart.add(inventory.get("Dior"), 1)

    yield full_cart
