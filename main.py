import random

from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()  

manager.add_product(Product("Laptop", 899.99, 10))
manager.add_product(Product("Mause", 24.50, 15))
manager.add_product(Product("Keyboard", 59.99, 5))



cart = Cart()
for product in random.sample(manager.products, 3):
    cart.add_product(product)

print("\nCart contents:")
cart.display_cart()
print(f"Total to pay: €{cart.calculate_total():.2f}")