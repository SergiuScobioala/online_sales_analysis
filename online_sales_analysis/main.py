from product import Product
from product_manager import ProductManager

manager = ProductManager()  

manager.add_product(Product("Laptop", 899.99, 5))
manager.add_product(Product("Mause", 24.50, 20))
manager.add_product(Product("Keyboard", 59.99, 10))

manager.display_all_products()
print(f"Total Inventory Value: ${manager.total_inventory_value():.2f}")

