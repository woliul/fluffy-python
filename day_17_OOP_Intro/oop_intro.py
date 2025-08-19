# Day 17: Introduction to Object-Oriented Programming (OOP) - Classes and Objects

# In OOP, a Class is a blueprint for creating objects.
# An Object is an instance of a Class.

# 1. Define a Class
class Dog:
    # The __init__ method is a special method called a constructor.
    # It runs whenever a new object is created from the class.
    # 'self' refers to the object itself.
    def __init__(self, name, breed):
        # These are attributes (data) of our object.
        self.name = name
        self.breed = breed
        self.is_hungry = True

    # 2. Define a Method
    # A method is a function that belongs to a class.
    def speak(self):
        print(f"{self.name} says Woof!")

    def eat(self):
        if self.is_hungry:
            print(f"{self.name} is eating now.")
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry.")

# 3. Create Objects (Instances of the Class)
# We create objects by calling the class name like a function.
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Poodle")

# 4. Access Attributes and Call Methods
print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
my_dog.speak()

print(f"Your dog's name is {your_dog.name} and she is a {your_dog.breed}.")
your_dog.speak()

# Let's interact with our objects
my_dog.eat()
my_dog.eat()  # Calling the method again to show attribute change
