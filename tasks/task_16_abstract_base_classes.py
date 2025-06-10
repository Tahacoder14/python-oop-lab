"""
Task 16: Abstract Base Classes (ABCs) - Defining Interfaces
Concept:
ABCs (from `abc` module) define "contracts" that concrete subclasses MUST implement.
Methods marked `@abstractmethod` must be overridden. ABCs with abstract methods
cannot be instantiated directly. This enforces an interface more strictly than duck typing.
Let's define a 'Drawable' interface for different shapes.
"""
from abc import ABC, abstractmethod

class Drawable(ABC): # Inherit from ABC
    def __init__(self, color):
        self.color = color
        print(f"Drawable interface part initialized with color: {self.color}")

    @abstractmethod # This method MUST be implemented by concrete subclasses
    def draw_on_canvas(self, canvas_name, x_pos, y_pos):
        """Draws the shape on a given canvas at specified coordinates."""
        pass

    @abstractmethod
    def calculate_area(self): # Another abstract method
        """Calculates and returns the area of the shape."""
        pass

    def get_color(self): # A concrete method, available to all subclasses
        return self.color

# Concrete subclass 1
class Circle(Drawable):
    def __init__(self, color, radius):
        super().__init__(color) # Call ABC's __init__
        self.radius = float(radius)
        print(f"Circle created: Radius {self.radius}, Color {self.color}")

    def draw_on_canvas(self, canvas_name, x_pos, y_pos): # Implementing abstract method
        print(f"Drawing a {self.color} Circle with radius {self.radius} on '{canvas_name}' at ({x_pos}, {y_pos}).")

    def calculate_area(self): # Implementing abstract method
        area = 3.14159 * (self.radius ** 2)
        print(f"Calculating area of Circle (radius {self.radius}): {area:.2f}")
        return area

# Concrete subclass 2
class Rectangle(Drawable):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)
        print(f"Rectangle created: W={self.width}, H={self.height}, Color {self.color}")

    def draw_on_canvas(self, canvas_name, x_pos, y_pos):
        print(f"Drawing a {self.color} Rectangle (W:{self.width}, H:{self.height}) on '{canvas_name}' at ({x_pos}, {y_pos}).")

    def calculate_area(self):
        area = self.width * self.height
        print(f"Calculating area of Rectangle (W:{self.width}, H:{self.height}): {area:.2f}")
        return area

def get_input_params():
    return [
        {"name": "circle_color", "label": "Circle Color:", "type": "selectbox", "options": ["Red", "Green", "Blue", "Yellow"], "default": "Red"},
        {"name": "circle_radius", "label": "Circle Radius:", "type": "number_input", "default": 5.0, "min_value":0.1, "step":0.5, "format":"%.1f"},
        {"name": "rect_color", "label": "Rectangle Color:", "type": "selectbox", "options": ["Red", "Green", "Blue", "Black"], "default": "Blue"},
        {"name": "rect_width", "label": "Rectangle Width:", "type": "number_input", "default": 8.0, "min_value":0.1, "step":0.5, "format":"%.1f"},
        {"name": "rect_height", "label": "Rectangle Height:", "type": "number_input", "default": 4.0, "min_value":0.1, "step":0.5, "format":"%.1f"},
        {"name": "canvas", "label": "Canvas Name:", "type": "text_input", "default": "MainDisplay"},
        {"name": "draw_x", "label": "Draw X Position:", "type": "number_input", "default": 10, "step":1, "format":"%d"},
        {"name": "draw_y", "label": "Draw Y Position:", "type": "number_input", "default": 20, "step":1, "format":"%d"},
    ]

def run_task(circle_color, circle_radius, rect_color, rect_width, rect_height, canvas, draw_x, draw_y):
    print("--- Attempting to instantiate the ABC (Drawable) directly ---")
    try:
        # d = Drawable("Purple") # This will raise TypeError
        # d.draw_on_canvas("Test",0,0)
        print("This line should not be reached if ABC is truly abstract.")
    except TypeError as e:
        print(f"Error caught (as expected): {e}\n  (Cannot instantiate abstract class Drawable with abstract methods draw_on_canvas, calculate_area)")

    print("\n--- Creating and using concrete Circle subclass ---")
    my_circle = Circle(circle_color, circle_radius)
    print(f"Circle color from get_color(): {my_circle.get_color()}")
    my_circle.draw_on_canvas(canvas, draw_x, draw_y)
    circle_area = my_circle.calculate_area()
    print(f"Returned circle area: {circle_area:.2f}")

    print("\n--- Creating and using concrete Rectangle subclass ---")
    my_rectangle = Rectangle(rect_color, rect_width, rect_height)
    my_rectangle.draw_on_canvas(canvas, draw_x + int(rect_width) + 10, draw_y) # Draw next to circle
    rect_area = my_rectangle.calculate_area()
    print(f"Returned rectangle area: {rect_area:.2f}")

    print("\n--- Polymorphism with ABCs ---")
    # All objects in this list are guaranteed to have draw_on_canvas and calculate_area
    drawables_list = [my_circle, my_rectangle]
    for i, item in enumerate(drawables_list):
        print(f"\nProcessing drawable item #{i+1} ({type(item).__name__}):")
        item.draw_on_canvas("SharedCanvas", 100 + i*50, 100 + i*50)
        item.calculate_area()

    print("\nABCs enforce a common interface, ensuring subclasses provide required methods.")

if __name__ == "__main__":
    run_task("Orange", 3.0, "Purple", 6.0, 9.0, "TestCanvas", 0, 0)
