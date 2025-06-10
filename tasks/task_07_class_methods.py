"""
Task 7: Class Methods (@classmethod) - Working with the Class Itself
Concept:
Class methods are bound to the class (not an instance). They receive the class
(`cls`) as the first argument. Useful for factory methods (alternative constructors)
or modifying class state. Let's manage a 'SoftwareLicense' pool.
"""

class SoftwareLicense:
    # Class attribute
    total_licenses_issued = 0
    available_license_types = ["Basic", "Pro", "Enterprise"]

    def __init__(self, user_name, license_type):
        if license_type not in SoftwareLicense.available_license_types:
            raise ValueError(f"Invalid license type: {license_type}. Choose from {SoftwareLicense.available_license_types}")
        self.user_name = user_name
        self.license_type = license_type
        self.license_id = f"{license_type.upper()}-{SoftwareLicense.total_licenses_issued + 1:03d}"
        SoftwareLicense.total_licenses_issued += 1
        print(f"License {self.license_id} ({self.license_type}) issued to {self.user_name}.")

    def display_info(self):
        print(f"-> User: {self.user_name}, License ID: {self.license_id}, Type: {self.license_type}")

    @classmethod
    def get_total_issued_count(cls):
        # cls refers to the SoftwareLicense class
        print(f"\nClass method 'get_total_issued_count' called on class: {cls.__name__}")
        return cls.total_licenses_issued

    @classmethod
    def create_basic_license(cls, user_name):
        # Factory method: an alternative way to create an instance
        print(f"\nClass method 'create_basic_license' (factory) called for {user_name}.")
        return cls(user_name, "Basic") # cls() calls __init__

    @classmethod
    def add_new_license_type(cls, new_type_name):
        if new_type_name not in cls.available_license_types:
            cls.available_license_types.append(new_type_name)
            print(f"\nNew license type '{new_type_name}' added. Available types: {cls.available_license_types}")
        else:
            print(f"\nLicense type '{new_type_name}' already exists.")

def get_input_params():
    return [
        {"name": "user1_name", "label": "User 1 Name:", "type": "text_input", "default": "Alice"},
        {"name": "user1_type", "label": "User 1 License Type:", "type": "selectbox", "options": SoftwareLicense.available_license_types, "default": "Pro"},
        {"name": "user2_name_basic", "label": "User 2 Name (for Basic Factory):", "type": "text_input", "default": "Bob"},
        {"name": "new_type_to_add", "label": "New License Type to Add (e.g., Student):", "type": "text_input", "default": "Student"}
    ]

def run_task(user1_name, user1_type, user2_name_basic, new_type_to_add):
    # Reset class state for consistent demo runs in Streamlit
    SoftwareLicense.total_licenses_issued = 0
    SoftwareLicense.available_license_types = ["Basic", "Pro", "Enterprise"] # Reset

    print(f"Initially, total licenses issued: {SoftwareLicense.get_total_issued_count()}")

    print("\n--- Issuing licenses directly ---")
    lic1 = SoftwareLicense(user1_name, user1_type)
    lic1.display_info()

    print("\n--- Issuing license using a class method (factory) ---")
    lic2 = SoftwareLicense.create_basic_license(user2_name_basic)
    lic2.display_info()

    print(f"\nAfter issuing, total licenses: {SoftwareLicense.get_total_issued_count()}")
    # Can also call on instance, but it still refers to the class
    print(f"(Called on instance lic1: {lic1.get_total_issued_count()})")

    print("\n--- Modifying class state using a class method ---")
    SoftwareLicense.add_new_license_type(new_type_to_add)
    if new_type_to_add and new_type_to_add not in ["Basic", "Pro", "Enterprise"]: # check if new type was actually added
        lic3 = SoftwareLicense("Charlie", new_type_to_add) # Try using the new type
        lic3.display_info()
        print(f"Total licenses now: {SoftwareLicense.get_total_issued_count()}")
    else:
        print(f"Skipping license creation for '{new_type_to_add}' as it might be a pre-existing type or empty.")


if __name__ == "__main__":
    run_task("Eve", "Enterprise", "Dave", "Trial")