"""
Task 1: Classes and Objects - The Blueprints of Your Code
Concept:
A CLASS is like a blueprint for creating things (objects).
An OBJECT is an actual thing created from that blueprint.
Let's create a custom 'Character' for a simple game!
"""

class Character:
    # Class attribute - shared by all characters
    game_world = "Mystica"

    def __init__(self, name, character_class, level):
        # Instance attributes - unique to each character object
        self.name = name
        self.character_class = character_class
        self.level = level
        print(f"Character '{self.name}' ({self.character_class} Lvl {self.level}) has entered {Character.game_world}!")

    def introduce(self):
        return f"Greetings! I am {self.name}, a Level {self.level} {self.character_class}."

    def level_up(self, levels_gained=1):
        self.level += levels_gained
        print(f"{self.name} leveled up! Now Level {self.level}.")
        return self.level

def get_input_params():
    return [
        {"name": "char_name", "label": "Enter Character Name:", "type": "text_input", "default": "Gandalf"},
        {"name": "char_class", "label": "Choose Character Class:", "type": "selectbox",
         "options": ["Wizard", "Warrior", "Rogue", "Cleric"], "default": "Wizard"},
        {"name": "char_level", "label": "Starting Level:", "type": "number_input", "default": 10, "min_value": 1, "step": 1, "format": "%d"}
    ]

def run_task(char_name, char_class, char_level):
    print(f"--- Creating your custom Character ---")
    player_char = Character(char_name, char_class, char_level)

    print("\n--- Interacting with your Character ---")
    print(player_char.introduce())

    print(f"\nYour character, {player_char.name}, is about to level up...")
    player_char.level_up(2) # Level up by 2

    print(f"\nAll characters exist in the game world: {Character.game_world}")
    print(f"Type of 'Character' (the blueprint): {type(Character)}")
    print(f"Type of '{player_char.name}' (an object): {type(player_char)}")

if __name__ == "__main__":
    run_task(char_name="Aragorn", char_class="Warrior", char_level=15)