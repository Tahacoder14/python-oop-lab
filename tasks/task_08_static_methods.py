"""
Task 8: Static Methods (@staticmethod) - Utilities within Your Class
Concept:
Static methods don't operate on instance (`self`) or class (`cls`) state.
They are like regular functions grouped under a class's namespace for organization.
Often used for utility functions. Let's create a 'MathUtils' class.
"""

class MathUtils:
    # This class might not even need an __init__ if it only has static methods.
    # We add one just to show it doesn't interfere with static methods.
    def __init__(self, precision=2):
        self.precision_digits = precision # Instance attribute, NOT used by static methods
        print(f"MathUtils instance created (precision for instance methods: {self.precision_digits}).")

    @staticmethod
    def add(x, y):
        print(f"Static method MathUtils.add({x}, {y}) called.")
        return x + y

    @staticmethod
    def multiply(x, y):
        print(f"Static method MathUtils.multiply({x}, {y}) called.")
        return x * y

    @staticmethod
    def is_even(number):
        print(f"Static method MathUtils.is_even({number}) called.")
        return number % 2 == 0

    # This is an INSTANCE method, for contrast
    def format_number(self, num):
        return f"{num:.{self.precision_digits}f}"


def get_input_params():
    return [
        {"name": "num_a", "label": "Number A for Add/Multiply:", "type": "number_input", "default": 10.5, "step":0.5, "format":"%.1f"},
        {"name": "num_b", "label": "Number B for Add/Multiply:", "type": "number_input", "default": 5.0, "step":0.5, "format":"%.1f"},
        {"name": "check_even_num", "label": "Number to Check if Even:", "type": "number_input", "default": 4, "step":1, "format":"%d"}
    ]

def run_task(num_a, num_b, check_even_num):
    print("--- Calling static methods directly on the MathUtils class ---")
    sum_result = MathUtils.add(num_a, num_b)
    print(f"Sum: {num_a} + {num_b} = {sum_result}")

    product_result = MathUtils.multiply(num_a, num_b)
    print(f"Product: {num_a} * {num_b} = {product_result}")

    even_check = MathUtils.is_even(check_even_num)
    print(f"Is {check_even_num} even? {even_check}")
    odd_num = check_even_num + 1
    print(f"Is {odd_num} even? {MathUtils.is_even(odd_num)}")

    print("\n--- Static methods can also be called on an instance (but don't use instance data) ---")
    instance_utils = MathUtils(precision=4) # Create an instance
    sum_via_instance = instance_utils.add(100, 200) # Still doesn't use 'precision_digits'
    print(f"Sum via instance call: {sum_via_instance}")

    print("\n--- Compare with an instance method that USES instance data ---")
    print(f"Instance method format_number(3.14159265): {instance_utils.format_number(3.14159265)}")


    print("\nKey takeaway: Static methods are like regular functions namespaced under the class.")
    print("They don't have access to 'self' (instance state) or 'cls' (class state).")

if __name__ == "__main__":
    run_task(num_a=7, num_b=3, check_even_num=10)