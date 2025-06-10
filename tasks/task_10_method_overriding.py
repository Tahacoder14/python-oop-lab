"""
Task 10: Method Overriding - Customizing Inherited Behavior
Concept:
Method overriding allows a subclass to provide its own version of a method
from its parent class. Experiment with different shapes and their area calculations.
"""

class Shape:
    def __init__(self, name="Shape"):
        self.name = name
        print(f"Shape '{self.name}' created.")

    def area(self):
        print(f"The area calculation is not defined for a generic '{self.name}'.")
        return 0

    def draw(self):
        print(f"Drawing a generic '{self.name}'.")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
        print(f"Rectangle with width {self.width} and height {self.height} created.")

    def area(self): # Overriding
        result = self.width * self.height
        print(f"Rectangle Area: width ({self.width}) * height ({self.height}) = {result}")
        return result

    def draw(self): # Overriding
        print(f"Drawing Rectangle: Four sides, four right angles.")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        self.pi = 3.14159
        print(f"Circle with radius {self.radius} created.")

    def area(self): # Overriding
        result = self.pi * (self.radius ** 2)
        print(f"Circle Area: π * radius ({self.radius})^2 = {result:.2f}")
        return result

    def draw(self): # Overriding
        print(f"Drawing Circle: A perfect round curve.")

def get_input_params():
    return [
        {"name": "rect_width", "label": "Rectangle Width:", "type": "number_input", "default": 5.0, "min_value": 0.1, "step": 0.5, "format": "%.1f"},
        {"name": "rect_height", "label": "Rectangle Height:", "type": "number_input", "default": 10.0, "min_value": 0.1, "step": 0.5, "format": "%.1f"},
        {"name": "circle_radius", "label": "Circle Radius:", "type": "number_input", "default": 7.0, "min_value": 0.1, "step": 0.5, "format": "%.1f"},
    ]

def run_task(rect_width, rect_height, circle_radius):
    print("--- Generic Shape (Base Class) ---")
    generic_shape = Shape("Abstract Form")
    generic_shape.draw()
    print(f"Generic shape area: {generic_shape.area()}")

    print("\n--- Your Custom Rectangle ---")
    rect = Rectangle(rect_width, rect_height)
    rect.draw()
    rect_area = rect.area()
    print(f"Rectangle area result: {rect_area}")

    print("\n--- Your Custom Circle ---")
    circ = Circle(circle_radius)
    circ.draw()
    circ_area = circ.area()
    print(f"Circle area result: {circ_area:.2f}")

    print("\n--- Polymorphism in action (demonstrating overriding) ---")
    shapes = [generic_shape, rect, circ]
    for shape_obj in shapes:
        print(f"\nProcessing shape: {shape_obj.name}")
        shape_obj.draw()
        current_area = shape_obj.area() # Calls the appropriate area() method
        print(f"Area for {shape_obj.name}: {current_area:.2f}")

if __name__ == "__main__":
    run_task(rect_width=6, rect_height=3, circle_radius=4)