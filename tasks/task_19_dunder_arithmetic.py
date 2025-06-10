"""
Task 19: Special Methods (Arithmetic) - Customizing Operators
Concept:
Define how standard arithmetic operators (+, -, *, etc.) work with your
custom objects by implementing methods like `__add__`, `__sub__`, `__mul__`.
Let's create a 'Currency' class that supports addition and scalar multiplication.
"""

class Currency:
    def __init__(self, amount, unit="USD"):
        self.amount = float(amount)
        self.unit = unit.upper()
        print(f"Currency object created: {self.amount:.2f} {self.unit}")

    def __str__(self):
        return f"{self.amount:.2f} {self.unit}"

    def __repr__(self):
        return f"Currency(amount={self.amount:.2f}, unit='{self.unit}')"

    def __add__(self, other): # For self + other
        print(f"Currency.__add__ called: {self} + {other}")
        if isinstance(other, Currency) and self.unit == other.unit:
            return Currency(self.amount + other.amount, self.unit)
        elif isinstance(other, Currency) and self.unit != other.unit:
            print(f"Error: Cannot add different currency units ({self.unit} and {other.unit}) directly.")
            return NotImplemented # Or raise an error
        elif isinstance(other, (int, float)): # Adding a raw number (assume same unit)
             print(f"Warning: Adding raw number {other} to {self.unit}. Assuming it's in {self.unit}.")
             return Currency(self.amount + other, self.unit)
        return NotImplemented

    def __sub__(self, other): # For self - other
        print(f"Currency.__sub__ called: {self} - {other}")
        if isinstance(other, Currency) and self.unit == other.unit:
            return Currency(self.amount - other.amount, self.unit)
        elif isinstance(other, Currency) and self.unit != other.unit:
            print(f"Error: Cannot subtract different currency units ({self.unit} and {other.unit}) directly.")
            return NotImplemented
        elif isinstance(other, (int, float)):
             print(f"Warning: Subtracting raw number {other} from {self.unit}. Assuming it's in {self.unit}.")
             return Currency(self.amount - other, self.unit)
        return NotImplemented

    def __mul__(self, scalar): # For self * scalar
        print(f"Currency.__mul__ called: {self} * {scalar}")
        if isinstance(scalar, (int, float)):
            return Currency(self.amount * scalar, self.unit)
        return NotImplemented

    def __rmul__(self, scalar): # For scalar * self (if scalar doesn't handle it)
        print(f"Currency.__rmul__ called: {scalar} * {self}")
        return self.__mul__(scalar) # Multiplication is often commutative

    def __eq__(self, other): # For self == other
        if isinstance(other, Currency):
            return self.amount == other.amount and self.unit == other.unit
        return False

def get_input_params():
    return [
        {"name": "amount1", "label": "Amount 1:", "type": "number_input", "default": 100.50, "step":0.01, "format":"%.2f"},
        {"name": "unit1", "label": "Unit 1 (e.g., USD, EUR):", "type": "text_input", "default": "USD"},
        {"name": "amount2", "label": "Amount 2 (for +,-):", "type": "number_input", "default": 50.25, "step":0.01, "format":"%.2f"},
        {"name": "unit2", "label": "Unit 2 (for +,-):", "type": "text_input", "default": "USD"},
        {"name": "scalar_val", "label": "Scalar for Multiplication:", "type": "number_input", "default": 2.5, "step":0.1, "format":"%.1f"},
        {"name": "raw_num_add", "label": "Raw Number to Add:", "type": "number_input", "default": 10.0, "step":0.1, "format":"%.1f"}
    ]

def run_task(amount1, unit1, amount2, unit2, scalar_val, raw_num_add):
    c1 = Currency(amount1, unit1)
    c2 = Currency(amount2, unit2)

    print("\n--- Addition (c1 + c2) ---")
    sum_result = c1 + c2
    if sum_result is not NotImplemented:
        print(f"Result: {c1} + {c2} = {sum_result}")
    else:
        print(f"Addition {c1} + {c2} is not supported (likely due to different units).")

    print(f"\n--- Addition with raw number (c1 + {raw_num_add}) ---")
    sum_raw_result = c1 + raw_num_add
    if sum_raw_result is not NotImplemented:
        print(f"Result: {c1} + {raw_num_add} = {sum_raw_result}")


    print("\n--- Subtraction (c1 - c2) ---")
    diff_result = c1 - c2
    if diff_result is not NotImplemented:
        print(f"Result: {c1} - {c2} = {diff_result}")
    else:
        print(f"Subtraction {c1} - {c2} is not supported.")


    print(f"\n--- Scalar Multiplication (c1 * {scalar_val}) ---")
    scaled_result = c1 * scalar_val
    if scaled_result is not NotImplemented:
        print(f"Result: {c1} * {scalar_val} = {scaled_result}")

    print(f"\n--- Right-hand Scalar Multiplication ({scalar_val} * c1) ---")
    r_scaled_result = scalar_val * c1 # Calls __rmul__
    if r_scaled_result is not NotImplemented:
        print(f"Result: {scalar_val} * {c1} = {r_scaled_result}")

    print("\n--- Equality Check ---")
    c3 = Currency(amount1, unit1) # Same as c1
    print(f"Is {c1} == {c2}? {c1 == c2}")
    print(f"Is {c1} == {c3}? {c1 == c3}")

if __name__ == "__main__":
    run_task(200.0, "EUR", 75.5, "EUR", 1.5, 20.0)
    run_task(100.0, "USD", 50.0, "CAD", 3.0, 5.0) # Test different units