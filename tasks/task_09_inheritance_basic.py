"""
Task 9: Basic Inheritance - Building on Existing Blueprints
Concept:
Inheritance allows a new class (child/subclass) to acquire properties and methods
from an existing class (parent/superclass). Create your own animal and a specialized pet!
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal '{self.name}' ({self.species}) created.")

    def speak(self):
        return "The animal makes a generic sound."

    def eat(self, food="food"):
        print(f"{self.name} the {self.species} is eating {food}.")

class Pet(Animal): # Changed Dog to a more generic Pet for user input
    def __init__(self, name, species, breed_or_trait):
        super().__init__(name, species)
        self.breed_or_trait = breed_or_trait
        print(f"Specifically, it's a {self.breed_or_trait} {self.species.lower()}.")

    def speak(self): # Overridden
        if self.species.lower() == "dog":
            return f"{self.name} says: Woof! Woof!"
        elif self.species.lower() == "cat":
            return f"{self.name} says: Meow!"
        else:
            return f"{self.name} the {self.species} makes a special sound!"

    def perform_trick(self, trick="sit"):
        print(f"{self.name} the {self.breed_or_trait} {self.species.lower()} performs the '{trick}' trick!")

def get_input_params():
    return [
        {"name": "animal_name", "label": "Generic Animal's Name:", "type": "text_input", "default": "Creature"},
        {"name": "animal_species", "label": "Generic Animal's Species:", "type": "text_input", "default": "Unknown"},
        {"name": "pet_name", "label": "Your Pet's Name:", "type": "text_input", "default": "Buddy"},
        {"name": "pet_species", "label": "Your Pet's Species (e.g., Dog, Cat):", "type": "selectbox",
         "options": ["Dog", "Cat", "Bird", "Lizard"], "default": "Dog"},
        {"name": "pet_trait", "label": "Your Pet's Breed/Trait (e.g., Labrador, Tabby, Agile):", "type": "text_input", "default": "Golden Retriever"},
        {"name": "pet_food", "label": "What does your pet eat?", "type": "text_input", "default": "kibble"},
        {"name": "pet_trick", "label": "What trick can your pet do?", "type": "text_input", "default": "fetch"},
    ]

def run_task(animal_name, animal_species, pet_name, pet_species, pet_trait, pet_food, pet_trick):
    print("--- Creating a generic Animal with your input ---")
    generic_creature = Animal(animal_name, animal_species)
    print(generic_creature.speak())
    generic_creature.eat("berries") # Generic food

    print(f"\n--- Creating your custom Pet: {pet_name} the {pet_species} ---")
    my_pet = Pet(pet_name, pet_species, pet_trait)
    print(f"Pet's name: {my_pet.name}")
    print(f"Pet's species: {my_pet.species}")
    print(f"Pet's specific trait: {my_pet.breed_or_trait}")
    print(my_pet.speak())
    my_pet.eat(pet_food)
    my_pet.perform_trick(pet_trick)

    print("\n--- Checking relationships ---")
    print(f"Is {my_pet.name} an instance of Pet? {isinstance(my_pet, Pet)}")
    print(f"Is {my_pet.name} an instance of Animal? {isinstance(my_pet, Animal)}")
    print(f"Is Pet a subclass of Animal? {issubclass(Pet, Animal)}")

if __name__ == "__main__":
    run_task("Critter", "Mysterious", "Rex", "Dog", "German Shepherd", "bones", "guard")