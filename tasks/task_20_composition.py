"""
Task 20: Composition - Building Complex Objects from Simpler Ones ("Has-A" Relationship)
Concept:
Composition involves creating complex objects by combining simpler ones.
A 'Computer' "has-a" CPU, RAM, and Storage. This is often preferred over
deep inheritance hierarchies for flexibility.
"""

# Part Class 1: CPU
class CPU:
    def __init__(self, model, cores, speed_ghz):
        self.model = model
        self.cores = int(cores)
        self.speed_ghz = float(speed_ghz)
        print(f"  CPU Part Created: {self.model}, {self.cores} cores, {self.speed_ghz:.1f} GHz")

    def get_specs(self):
        return f"CPU: {self.model} ({self.cores} Cores @ {self.speed_ghz:.1f} GHz)"

# Part Class 2: RAM
class RAM:
    def __init__(self, capacity_gb, ram_type="DDR4"):
        self.capacity_gb = int(capacity_gb)
        self.type = ram_type
        print(f"  RAM Part Created: {self.capacity_gb}GB {self.type}")

    def get_specs(self):
        return f"RAM: {self.capacity_gb}GB {self.type}"

# Part Class 3: Storage
class Storage:
    def __init__(self, capacity_gb, storage_type="SSD"):
        self.capacity_gb = int(capacity_gb)
        self.type = storage_type
        print(f"  Storage Part Created: {self.capacity_gb}GB {self.type}")

    def get_specs(self):
        return f"Storage: {self.capacity_gb}GB {self.type}"

# Whole Class: Computer (composed of CPU, RAM, Storage)
class Computer:
    def __init__(self, computer_name, cpu_model, cpu_cores, cpu_speed,
                 ram_capacity, storage_capacity, storage_type_val="SSD"):
        self.name = computer_name
        print(f"\n--- Assembling Computer: {self.name} ---")

        # Composition: Computer creates and "owns" its component instances
        self.cpu = CPU(cpu_model, cpu_cores, cpu_speed)
        self.ram = RAM(ram_capacity) # Using default RAM type
        self.storage = Storage(storage_capacity, storage_type_val)
        print(f"--- Computer '{self.name}' Assembly Complete ---")

    def boot_up(self):
        print(f"\nBooting up {self.name}...")
        print("  Checking components:")
        print(f"  {self.cpu.get_specs()}")
        print(f"  {self.ram.get_specs()}")
        print(f"  {self.storage.get_specs()}")
        print(f"{self.name} is now ON and ready!")

    def run_application(self, app_name):
        print(f"{self.name} is running application: '{app_name}'")
        print(f"  Utilizing {self.cpu.cores} CPU cores and part of {self.ram.capacity_gb}GB RAM.")

def get_input_params():
    return [
        {"name": "comp_name", "label": "Computer Name:", "type": "text_input", "default": "MyWorkstation"},
        {"name": "cpu_m", "label": "CPU Model:", "type": "text_input", "default": "Intel i7-12700K"},
        {"name": "cpu_c", "label": "CPU Cores:", "type": "number_input", "default": 12, "min_value":1, "step":1, "format":"%d"},
        {"name": "cpu_s", "label": "CPU Speed (GHz):", "type": "number_input", "default": 3.6, "min_value":0.1, "step":0.1, "format":"%.1f"},
        {"name": "ram_cap", "label": "RAM Capacity (GB):", "type": "selectbox", "options": [8, 16, 32, 64], "default": 16},
        {"name": "stor_cap", "label": "Storage Capacity (GB):", "type": "selectbox", "options": [256, 512, 1000, 2000], "default": 512}, # 1000 for 1TB
        {"name": "stor_type", "label": "Storage Type:", "type": "selectbox", "options": ["SSD", "NVMe SSD", "HDD"], "default": "SSD"},
        {"name": "app_to_run", "label": "Application to Run:", "type": "text_input", "default": "Code Editor"},
    ]

def run_task(comp_name, cpu_m, cpu_c, cpu_s, ram_cap, stor_cap, stor_type, app_to_run):
    my_computer = Computer(comp_name, cpu_m, cpu_c, cpu_s, ram_cap, stor_cap, stor_type)
    my_computer.boot_up()
    my_computer.run_application(app_to_run)

    print("\n--- Accessing parts of the computer ---")
    print(f"Your computer's CPU details: {my_computer.cpu.get_specs()}")
    print(f"Your computer's RAM capacity: {my_computer.ram.capacity_gb}GB")

    print("\nComposition allows building complex objects by combining simpler, specialized parts.")
    print("This makes systems more modular and easier to manage/update.")

if __name__ == "__main__":
    run_task("GamingRig", "AMD Ryzen 9", 16, 4.0, 32, 1000, "NVMe SSD", "Cyberpunk 2077")