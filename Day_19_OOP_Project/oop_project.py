# Day 19: OOP Project - Fantasy Character Creator

# Parent Class
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")

# Child Classes inheriting from Character
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 10
        self.health = 120 # Warriors have more health

    def attack(self):
        print(f"{self.name} swings a mighty sword, dealing {self.strength * 2} damage!")

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.intelligence = 12
        self.mana = 80 # Wizards have more mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts a fiery spell! Mana remaining: {self.mana}")
        else:
            print(f"{self.name} doesn't have enough mana to cast the spell.")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name)
        self.stealth = 15

    def sneak_attack(self):
        print(f"{self.name} disappears into the shadows and performs a sneak attack!")
        self.health -= 5 # Rogues take a bit of health to do a sneak attack
        print(f"New health: {self.health}")


# Main program logic
def create_character():
    print("Welcome to the Character Creator!")
    name = input("Enter your character's name: ")

    while True:
        choice = input("Choose a class (Warrior, Wizard, Rogue): ").lower()
        if choice == "warrior":
            return Warrior(name)
        elif choice == "wizard":
            return Wizard(name)
        elif choice == "rogue":
            return Rogue(name)
        else:
            print("Invalid choice. Please choose from Warrior, Wizard, or Rogue.")

# Create and test the character
player_character = create_character()
print("\nCharacter created successfully!")
player_character.display_stats()

if isinstance(player_character, Warrior):
    player_character.attack()
elif isinstance(player_character, Wizard):
    player_character.cast_spell()
    player_character.cast_spell()
elif isinstance(player_character, Rogue):
    player_character.sneak_attack()
