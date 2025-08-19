# Day 18: OOP Inheritance - Inheriting Attributes and Methods

# Inheritance is a mechanism that allows a new class (child) to inherit
# from an existing class (parent).

# 1. The Parent Class (Base Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The animal makes a sound.")

# 2. The Child Class (Derived Class)
# The new class inherits from the parent by passing the parent's name in parentheses.
class Dog(Animal):
    def __init__(self, name, breed):
        # The super() function calls the parent's __init__ method.
        # This allows the child class to inherit the parent's attributes.
        super().__init__(name, species="Dog")
        self.breed = breed

    # A child class can override a parent's method with its own implementation.
    def make_sound(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Another child class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        print(f"{self.name} says Meow!")

# 3. Creating Objects and Using Inheritance
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "White")

print(f"My dog is a {my_dog.species} named {my_dog.name}.")
my_dog.make_sound() # Calls the child's method
my_dog.fetch()

print(f"My cat is a {my_cat.species} named {my_cat.name}.")
my_cat.make_sound() # Calls the child's method

# The parent class still works
generic_animal = Animal("Zoe", "Unknown")
generic_animal.make_sound()
