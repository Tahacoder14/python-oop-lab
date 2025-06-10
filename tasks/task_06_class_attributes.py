"""
Task 6: Class Attributes - Shared Data for All Instances
Concept:
Class attributes are shared by ALL instances of a class.
Modifying a class attribute affects all objects of that class.
Let's make pizzas and see how a shared setting (like baking temperature) applies to all.
"""

class Pizza:
    # Class attributes
    default_oven_temperature_celsius = 220  # Shared by all pizzas
    pizzas_made_count = 0                 # Shared counter

    def __init__(self, name, toppings_list):
        # Instance attributes
        self.name = name
        self.toppings = toppings_list
        Pizza.pizzas_made_count += 1
        print(f"Pizza '{self.name}' with {', '.join(self.toppings)} created. (Pizza #{Pizza.pizzas_made_count})")

    def describe(self):
        print(f"-> '{self.name}': Toppings: {', '.join(self.toppings)}. "
              f"Bake at {Pizza.default_oven_temperature_celsius}°C (current class setting).")

    @classmethod
    def update_oven_temperature(cls, new_temp):
        print(f"\nUpdating default oven temperature for ALL pizzas from {cls.default_oven_temperature_celsius}°C to {new_temp}°C.")
        cls.default_oven_temperature_celsius = int(new_temp)

def get_input_params():
    return [
        {"name": "pizza1_name", "label": "Pizza 1 Name:", "type": "text_input", "default": "Margherita"},
        {"name": "pizza1_toppings_str", "label": "Pizza 1 Toppings (comma-separated):", "type": "text_input", "default": "Tomato Sauce,Mozzarella,Basil"},
        {"name": "pizza2_name", "label": "Pizza 2 Name:", "type": "text_input", "default": "Pepperoni Feast"},
        {"name": "pizza2_toppings_str", "label": "Pizza 2 Toppings (comma-separated):", "type": "text_input", "default": "Tomato Sauce,Mozzarella,Pepperoni,Sausage"},
        {"name": "new_temp", "label": "Set New Oven Temperature (°C for all pizzas):", "type": "slider", "default": 220, "min_value": 180, "max_value": 250, "step": 5, "format":"%d"}
    ]

def run_task(pizza1_name, pizza1_toppings_str, pizza2_name, pizza2_toppings_str, new_temp):
    print(f"Initial class attribute - Default Oven Temp: {Pizza.default_oven_temperature_celsius}°C")
    print(f"Initial class attribute - Pizzas Made: {Pizza.pizzas_made_count}") # Might show count from previous runs if module isn't fully reloaded by Streamlit

    # Reset counter for clarity in this run if needed (though Streamlit usually reloads modules)
    Pizza.pizzas_made_count = 0

    toppings1 = [t.strip() for t in pizza1_toppings_str.split(',') if t.strip()]
    toppings2 = [t.strip() for t in pizza2_toppings_str.split(',') if t.strip()]

    print("\n--- Creating Pizzas with Current Class Settings ---")
    p1 = Pizza(pizza1_name, toppings1)
    p2 = Pizza(pizza2_name, toppings2)

    p1.describe()
    p2.describe()
    print(f"Total pizzas made in this run: {Pizza.pizzas_made_count}")

    # User updates the class attribute
    Pizza.update_oven_temperature(new_temp)

    print("\n--- Describing Pizzas AFTER Class Attribute Change ---")
    p1.describe() # Will show the new temperature
    p2.describe() # Will also show the new temperature

    print("\n--- Instance vs. Class Attribute ---")
    # If an instance assigns to an attribute with the same name as a class attribute,
    # it creates an INSTANCE attribute that shadows the class one for THAT instance.
    print(f"Shadowing: Assigning '{p1.name}.default_oven_temperature_celsius = 200' (creates instance attribute)")
    p1.default_oven_temperature_celsius = 200 # This creates an instance attribute on p1
    print(f"p1's temperature (instance): {p1.default_oven_temperature_celsius}°C")
    print(f"p2's temperature (class): {p2.default_oven_temperature_celsius}°C (still using class attribute)")
    print(f"Pizza class default temperature: {Pizza.default_oven_temperature_celsius}°C (class attribute unchanged by p1's instance attribute)")

if __name__ == "__main__":
    run_task("Veggie Delight", "Mushrooms,Peppers,Onions", "Meat Lover", "Pepperoni,Ham,Bacon", 230)