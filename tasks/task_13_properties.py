"""
Task 13: Properties (@property) - Smart Attributes with Getters
Concept:
`@property` lets you define methods that are accessed like attributes (no `()`).
Useful for computed values or controlled read-access.
Let's model a 'Rectangle' where area and perimeter are properties.
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = float(width)  # Internal "private" attribute
        self._height = float(height) # Internal "private" attribute
        print(f"Rectangle created with Width: {self._width}, Height: {self._height}")

    @property
    def width(self): # Getter for width
        print("Getting width using @property...")
        return self._width

    @property
    def height(self): # Getter for height
        print("Getting height using @property...")
        return self._height

    @property
    def area(self): # Computed property
        print("Calculating area using @property...")
        return self._width * self._height

    @property
    def perimeter(self): # Computed property
        print("Calculating perimeter using @property...")
        return 2 * (self._width + self._height)

    # No setters defined here, so width, height, area, perimeter are effectively read-only
    # after object creation via these properties.

def get_input_params():
    return [
        {"name": "rect_width", "label": "Rectangle Width:", "type": "number_input", "default": 10.0, "min_value":0.1, "step":0.5, "format":"%.1f"},
        {"name": "rect_height", "label": "Rectangle Height:", "type": "number_input", "default": 5.0, "min_value":0.1, "step":0.5, "format":"%.1f"}
    ]

def run_task(rect_width, rect_height):
    my_rectangle = Rectangle(rect_width, rect_height)

    print("\n--- Accessing properties (like attributes) ---")
    print(f"Width: {my_rectangle.width}")   # Calls width() getter
    print(f"Height: {my_rectangle.height}") # Calls height() getter
    print(f"Area: {my_rectangle.area}")     # Calls area() getter (computed)
    print(f"Perimeter: {my_rectangle.perimeter}") # Calls perimeter() getter (computed)

    print("\n--- Attempting to set a property without a setter (will fail) ---")
    try:
        print("Attempting: my_rectangle.area = 100")
        my_rectangle.area = 100
    except AttributeError as e:
        print(f"Error caught (as expected): {e}")

    print("\n--- Internal attributes can still be accessed (if not truly private) ---")
    print(f"Internal _width: {my_rectangle._width}")
    # my_rectangle._width = 20 # This would change it, bypassing property logic if any existed in a setter
    # print(f"After changing _width directly, new area: {my_rectangle.area}")

    print("\nProperties provide a clean interface and allow future changes to internal logic")
    print("without breaking how users access the data (e.g., add validation in a setter later).")

if __name__ == "__main__":
    run_task(rect_width=8, rect_height=4)