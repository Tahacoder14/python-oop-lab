"""
Task 5: __str__ and __repr__ - Readable Object Representations
Concept:
- `__str__(self)`: User-friendly string (e.g., for `print()`).
- `__repr__(self)`: Developer-friendly, unambiguous string (e.g., for debugging, should ideally allow `eval(repr(obj)) == obj`).
Create a 'Product' and see how its string representations differ.
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = float(price)

    def __str__(self):
        # User-friendly: "Product: <Name> (ID: <ID>), Price: $<Price>"
        return f"Product: {self.name} (ID: {self.product_id}), Price: ${self.price:.2f}"

    def __repr__(self):
        # Developer-friendly: "Product(product_id='<ID>', name='<Name>', price=<Price>)"
        # This format aims to be something you could use to reconstruct the object.
        return f"Product(product_id='{self.product_id}', name='{self.name}', price={self.price:.2f})"

def get_input_params():
    return [
        {"name": "prod_id", "label": "Product ID:", "type": "text_input", "default": "XYZ123"},
        {"name": "prod_name", "label": "Product Name:", "type": "text_input", "default": "Wireless Mouse"},
        {"name": "prod_price", "label": "Price:", "type": "number_input", "default": 29.99, "min_value":0.01, "step":0.50, "format":"%.2f"}
    ]

def run_task(prod_id, prod_name, prod_price):
    my_product = Product(prod_id, prod_name, prod_price)

    print("--- Demonstrating __str__ (used by print()) ---")
    print(my_product) # This implicitly calls my_product.__str__()

    print("\n--- Demonstrating str() explicitly ---")
    str_representation = str(my_product)
    print(f"str(my_product) gives: {str_representation}")

    print("\n--- Demonstrating __repr__ (used by repr() and in collections) ---")
    repr_representation = repr(my_product)
    print(f"repr(my_product) gives: {repr_representation}")

    print("\n--- How __repr__ looks inside a list ---")
    product_list = [my_product, Product("ABC789", "Keyboard", 75.00)]
    print(product_list) # Elements in list usually show their __repr__

    print("\nIf __str__ is missing, print() and str() fall back to using __repr__.")
    class SimpleProduct:
        def __init__(self, name): self.name = name
        def __repr__(self): return f"SimpleProduct(name='{self.name}')"
    
    simple_prod = SimpleProduct("Basic Pen")
    print(f"\nSimpleProduct (only __repr__ defined):")
    print(simple_prod) # Uses __repr__
    print(repr(simple_prod)) # Uses __repr__

if __name__ == "__main__":
    run_task(prod_id="CPU001", prod_name="SuperFast CPU", prod_price=399.50)