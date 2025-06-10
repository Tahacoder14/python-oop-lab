"""
Task 2: The __init__ Method - Your Object's Welcome Party
Concept:
The `__init__` method (constructor) initializes a new object.
It sets up the object's initial state (attributes).
Let's build a custom 'Robot' with specific startup parameters.
"""

class Robot:
    def __init__(self, model_name, energy_level, task_specialty):
        self.model_name = model_name
        self.energy_level = float(energy_level) # Ensure it's a float
        self.task_specialty = task_specialty
        self.is_active = False
        print(f"Robot Model '{self.model_name}' initialized.")
        print(f"  Initial Energy: {self.energy_level:.1f}%")
        print(f"  Specialty: {self.task_specialty}")

    def activate(self):
        if self.energy_level > 10:
            self.is_active = True
            print(f"{self.model_name} is now ACTIVE.")
        else:
            print(f"{self.model_name} has low energy ({self.energy_level:.1f}%). Cannot activate.")

    def perform_task(self, task_description):
        if self.is_active:
            if self.energy_level >= 5:
                print(f"{self.model_name} performing task: '{task_description}' (related to {self.task_specialty}).")
                self.energy_level -= 5
                print(f"  Energy remaining: {self.energy_level:.1f}%")
            else:
                print(f"{self.model_name} has insufficient energy for '{task_description}'.")
        else:
            print(f"{self.model_name} is not active. Activate first.")

def get_input_params():
    return [
        {"name": "robot_model", "label": "Robot Model Name:", "type": "text_input", "default": "R2-D2"},
        {"name": "initial_energy", "label": "Initial Energy Level (0-100%):", "type": "slider", "default": 75.0, "min_value": 0.0, "max_value": 100.0, "step": 5.0, "format":"%.1f"},
        {"name": "robot_specialty", "label": "Robot's Task Specialty:", "type": "selectbox",
         "options": ["Navigation", "Repair", "Translation", "Combat"], "default": "Navigation"},
        {"name": "task_to_perform", "label": "Task for Robot to Perform:", "type": "text_input", "default": "Chart a course to Alderaan"}
    ]

def run_task(robot_model, initial_energy, robot_specialty, task_to_perform):
    print(f"--- Building your Robot: {robot_model} ---")
    my_robot = Robot(robot_model, initial_energy, robot_specialty)

    print("\n--- Operating your Robot ---")
    my_robot.activate()
    my_robot.perform_task(task_to_perform)
    my_robot.perform_task("Self-diagnostics") # Another task

    # Try a task that might deplete energy
    if my_robot.energy_level < 15 and my_robot.is_active:
        print(f"\n{my_robot.model_name} attempting a high-energy task...")
        my_robot.perform_task("Emergency power reroute")

if __name__ == "__main__":
    run_task(robot_model="Unit-01", initial_energy=60.0, robot_specialty="Repair", task_to_perform="Fix hyperdrive")