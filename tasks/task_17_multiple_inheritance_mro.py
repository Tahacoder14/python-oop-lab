"""
Task 17: Multiple Inheritance & Method Resolution Order (MRO)
Concept:
A class can inherit from multiple parent classes. Python's MRO (C3 Linearization)
determines the order in which methods are searched in the inheritance hierarchy.
`super()` follows this MRO. Let's build a 'FlyingCar'.
"""

class LandVehicle:
    def __init__(self, num_wheels, *args, **kwargs): # *args, **kwargs for super()
        super().__init__(*args, **kwargs) # Call next in MRO
        self.num_wheels = int(num_wheels)
        print(f"LandVehicle initialized: {self.num_wheels} wheels.")

    def drive(self, destination):
        print(f"Driving on {self.num_wheels} wheels to {destination}.")

    def identify(self):
        print("I am a LandVehicle.")

class AirVehicle:
    def __init__(self, max_altitude_ft, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_altitude = int(max_altitude_ft)
        print(f"AirVehicle initialized: Max altitude {self.max_altitude} ft.")

    def fly(self, destination):
        print(f"Flying at up to {self.max_altitude} ft towards {destination}.")

    def identify(self): # Also has identify
        print("I am an AirVehicle.")

# FlyingCar inherits from AirVehicle first, then LandVehicle
# The order here affects the MRO.
class FlyingCar(AirVehicle, LandVehicle): # MRO: FlyingCar -> AirVehicle -> LandVehicle -> object
    def __init__(self, model_name, num_wheels, max_altitude_ft, company):
        self.model = model_name
        self.company = company
        print(f"\n--- Constructing FlyingCar '{self.model}' by {self.company} ---")
        # super() will call __init__ of AirVehicle, then LandVehicle, due to MRO
        super().__init__(num_wheels=num_wheels, max_altitude_ft=max_altitude_ft)
        print(f"FlyingCar '{self.model}' construction complete.")

    def switch_mode(self, mode): # "land" or "air"
        if mode.lower() == "air":
            print(f"{self.model}: Engaging flight systems. Wheels retracting (conceptually!).")
        elif mode.lower() == "land":
            print(f"{self.model}: Engaging driving systems. Wings folding (conceptually!).")
        else:
            print(f"{self.model}: Unknown mode '{mode}'.")

    # Overriding identify to show it comes from FlyingCar first
    def identify(self):
        print(f"I am a {self.model} FlyingCar by {self.company}.")
        print("  Calling super().identify() to see next in MRO:")
        super().identify() # This will call AirVehicle.identify() due to MRO

def get_input_params():
    return [
        {"name": "fc_model", "label": "Flying Car Model:", "type": "text_input", "default": "SkyCruiser X1"},
        {"name": "fc_wheels", "label": "Number of Wheels:", "type": "number_input", "default": 4, "min_value":3, "step":1, "format":"%d"},
        {"name": "fc_altitude", "label": "Max Flight Altitude (ft):", "type": "number_input", "default": 10000, "min_value":1000, "step":1000, "format":"%d"},
        {"name": "fc_company", "label": "Manufacturer Company:", "type": "text_input", "default": "AeroAuto Inc."},
        {"name": "drive_dest", "label": "Driving Destination:", "type": "text_input", "default": "City Center"},
        {"name": "fly_dest", "label": "Flying Destination:", "type": "text_input", "default": "Mountain Resort"},
    ]

def run_task(fc_model, fc_wheels, fc_altitude, fc_company, drive_dest, fly_dest):
    my_flying_car = FlyingCar(fc_model, fc_wheels, fc_altitude, fc_company)

    print("\n--- Identifying the FlyingCar ---")
    my_flying_car.identify() # Calls FlyingCar's, then AirVehicle's identify via super()

    print("\n--- Operating the FlyingCar ---")
    my_flying_car.switch_mode("land")
    my_flying_car.drive(drive_dest) # Inherited from LandVehicle

    my_flying_car.switch_mode("air")
    my_flying_car.fly(fly_dest)   # Inherited from AirVehicle

    print("\n--- Method Resolution Order (MRO) for FlyingCar ---")
    # .mro() returns a list of classes in the order they are checked.
    print(FlyingCar.mro())
    # Or for a more readable format:
    # for cls_in_mro in FlyingCar.mro():
    #     print(f"  -> {cls_in_mro.__name__}")

    print("\nMultiple inheritance can be powerful but use with caution to avoid complexity.")
    print("`super()` is key to making it work cooperatively.")

if __name__ == "__main__":
    run_task("AeroDasher", 4, 15000, "FutureTrans", "Local Airport", "Neighboring Island")