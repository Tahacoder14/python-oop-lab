"""
Task 14: Setters & Deleters - Controlling Attribute Changes
Concept:
Building on `@property` (getter), `@<prop_name>.setter` controls assignment,
and `@<prop_name>.deleter` controls `del` operations.
Let's manage a 'User' with a validated email and an age that must be positive.
"""

class User:
    def __init__(self, username, initial_email, initial_age):
        self.username = username # Public, simple attribute
        self._email = None       # Internal storage for email
        self._age = None         # Internal storage for age

        # Use setters during initialization to apply validation
        self.email = initial_email
        self.age = initial_age
        print(f"User '{self.username}' created.")
        self.display_info()

    @property
    def email(self):
        print(f"Getting email for {self.username}: {self._email}")
        return self._email

    @email.setter
    def email(self, new_email):
        print(f"Attempting to set email for {self.username} to '{new_email}'...")
        if "@" in new_email and "." in new_email.split('@')[-1]:
            self._email = new_email
            print(f"Email for {self.username} set to: {self._email}")
        else:
            print(f"Invalid email format: '{new_email}'. Email not changed from '{self._email}'.")

    @email.deleter
    def email(self):
        print(f"Deleting email for {self.username} (was: {self._email})...")
        self._email = None
        print(f"Email for {self.username} cleared.")

    @property
    def age(self):
        print(f"Getting age for {self.username}: {self._age}")
        return self._age

    @age.setter
    def age(self, new_age):
        new_age = int(new_age) # Ensure it's an int
        print(f"Attempting to set age for {self.username} to {new_age}...")
        if new_age > 0:
            self._age = new_age
            print(f"Age for {self.username} set to: {self._age}")
        else:
            print(f"Invalid age: {new_age}. Age must be positive. Age not changed from {self._age}.")

    def display_info(self):
        print(f"-> User: {self.username}, Email: {self._email if self._email else 'N/A'}, Age: {self._age if self._age else 'N/A'}")

def get_input_params():
    return [
        {"name": "uname", "label": "Username:", "type": "text_input", "default": "john_doe"},
        {"name": "init_email", "label": "Initial Email:", "type": "text_input", "default": "john.doe@example.com"},
        {"name": "init_age", "label": "Initial Age:", "type": "number_input", "default": 30, "min_value":1, "step":1, "format":"%d"},
        {"name": "new_email_to_set", "label": "New Email to Try Setting:", "type": "text_input", "default": "johndoe_new@mail.co"},
        {"name": "invalid_email_to_set", "label": "Invalid Email to Try:", "type": "text_input", "default": "bademailformat"},
        {"name": "new_age_to_set", "label": "New Age to Try Setting:", "type": "number_input", "default": 35, "min_value":-10, "step":1, "format":"%d"},
    ]

def run_task(uname, init_email, init_age, new_email_to_set, invalid_email_to_set, new_age_to_set):
    print("--- Creating User with initial validation via setters ---")
    user1 = User(uname, init_email, init_age)

    print("\n--- Testing Email Setter (valid and invalid) ---")
    user1.email = new_email_to_set  # Calls @email.setter
    user1.display_info()
    user1.email = invalid_email_to_set # Try invalid
    user1.display_info()

    print("\n--- Testing Age Setter (valid and invalid) ---")
    user1.age = new_age_to_set  # Calls @age.setter
    user1.display_info()
    user1.age = -5 # Try invalid age
    user1.display_info()

    print("\n--- Testing Email Deleter ---")
    del user1.email # Calls @email.deleter
    user1.display_info()

    print("\nSetters provide controlled modification, deleters controlled removal.")

if __name__ == "__main__":
    run_task("test_user", "test@domain.com", 25, "valid_new@server.net", "no_at_sign", 0)
