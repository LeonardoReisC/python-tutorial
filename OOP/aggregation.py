# Generally, aggregation comprises one-to-many relationships
# Each objects has its own lifecycle
class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])

    def insert_products(self, *products):
        self._products.extend(products)

    def list_products(self):
        for product in self._products:
            print(product.name, product.price)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
p1, p2 = Product("Pen", 1.20), Product("Notebook", 10)
cart.insert_products(p1, p2)
cart.list_products()
print(cart.total())
