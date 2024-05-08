class Product:
    def __init__(self, product_id, name, category, price):
        self._product_id = product_id  # Приватне поле
        self._name = name  # Приватне поле
        self._category = category  # Приватне поле
        self._price = price  # Приватне поле

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_price(self):
        return self._price
class InventoryManagement:
    def __init__(self, products):
        self.products = products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def print_product_details(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")
        else:
            print("Product not found")
