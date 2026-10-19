"""Shopping cart module (system under test).

Specification:

Product(name, price, stock)
    A product: name, unit price (ILS), and the number of units in stock.

Inventory(products)
    A warehouse holding a list of products.
    - get(name): returns the product by name. An unknown product raises KeyError.
    - reserve(name, qty): removes qty units from the product's stock.
      If there is not enough stock, raises ValueError("not enough stock").
    - release(name, qty): returns qty units to the product's stock.

Cart(inventory)
    A shopping cart that works against a warehouse.
    - add(product, qty): adds qty units of the product to the cart and reserves
      them in the warehouse (reserve).
      If qty is less than 1 or greater than the product's current stock,
      raises ValueError("invalid quantity").
      Adding a product that is already in the cart increases its quantity.
    - remove(name): removes the product from the cart (the whole quantity) and
      returns the units to the warehouse (release).
      If the product is not in the cart, raises ValueError("product not in cart").
    - item_count(): returns the number of units in the cart (sum of all quantities).
    - total(): returns the amount to pay as a float, after the coupon discount
      if one was applied. The total is always calculated from what is in the
      cart right now.
    - apply_coupon(code): applies a coupon to the cart.
      SAVE10 - 10% discount.
      SAVE50 - 50% discount, only when the cart total is above 200 ILS
               (exactly 200 does not get the discount).
               If the total is not above 200, raises ValueError("cart total too low").
      An unknown code raises ValueError("unknown coupon").
"""

COUPONS = {"SAVE10": 0.10, "SAVE50": 0.50}


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    def __init__(self, products):
        self._products = {p.name: p for p in products}

    def get(self, name):
        return self._products[name]

    def reserve(self, name, qty):
        product = self._products[name]
        if qty > product.stock:
            raise ValueError("not enough stock")
        product.stock -= qty

    def release(self, name, qty):
        self._products[name].stock += qty


class Cart:
    def __init__(self, inventory):
        self._inventory = inventory
        self._items = {}  # name -> [product, qty]
        self._discount = 0.0

    def add(self, product, qty):
        if qty < 1 or qty > product.stock:
            raise ValueError("invalid quantity")
        self._inventory.reserve(product.name, qty)
        if product.name in self._items:
            self._items[product.name][1] += qty
        else:
            self._items[product.name] = [product, qty]

    def remove(self, name):
        if name not in self._items:
            return
        product, qty = self._items.pop(name)
        self._inventory.release(name, qty)

    def item_count(self):
        return sum(qty for _, qty in self._items.values())

    def _subtotal(self):
        return float(sum(p.price * qty for p, qty in self._items.values()))

    def total(self):
        return self._subtotal() - self._discount

    def apply_coupon(self, code):
        if code not in COUPONS:
            raise ValueError("unknown coupon")
        subtotal = self._subtotal()
        if code == "SAVE50" and subtotal < 200:
            raise ValueError("cart total too low")
        self._discount = subtotal * COUPONS[code]
