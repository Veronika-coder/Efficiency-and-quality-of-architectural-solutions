class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

def search_product(products, query):
    # Пошук товару за запитом
    found_products = []
    for product in products:
        if query.lower() in product.name.lower():
            found_products.append(product)
    return found_products

def display_product(product):
    # Відображення інформації про товар
    print(f"Name: {product.name}")
    print(f"Price: {product.price}")
    print(f"Type: {product.type}")

def order_product(product, quantity):
    # Замовлення товару
    total_price = product.price * quantity
    print(f"Ordered {product.name}, Quantity: {quantity}, Total Price: {total_price}")

# Приклад використання
products = [
    Product("Apple", 1.5, "Fruit"),
    Product("Banana", 0.5, "Fruit"),
    Product("Milk", 2.0, "Dairy"),
    Product("Bread", 1.0, "Bakery")
]

query = "apple"
found_products = search_product(products, query)
for product in found_products:
    display_product(product)

order_product(products[0], 3)
