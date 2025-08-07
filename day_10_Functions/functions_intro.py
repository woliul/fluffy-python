# Day 10: Functions - Reusable Blocks of Code

# Functions are blocks of code that perform a specific task.
# They help organize your code and make it reusable.

# 1. Defining a simple function with no parameters
def say_hello():
    """This function simply prints a greeting."""
    print("Hello, Python learner!")

# 2. Calling the function
# To run the code inside the function, you must call it by its name.
print("Calling the function for the first time:")
say_hello()

print("\nCalling it again:")
say_hello()

# 3. Defining a function with parameters
# Parameters are variables that the function accepts as input.
def greet_user(name):
    """This function greets a user by their name."""
    print(f"Hello, {name}! Welcome to Day 10.")

# 4. Calling the function with an argument
# 'Alice' is the argument passed to the 'name' parameter.
print("\nCalling greet_user with a name:")
greet_user("Alice")
greet_user("Woliul")

# 5. A function that returns a value
# The 'return' keyword sends a value back to the caller.
def add_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    sum_result = a + b
    return sum_result

# 6. Using the returned value
print("\nCalling add_numbers:")
result = add_numbers(5, 7)
print(f"The result of adding 5 and 7 is: {result}")

# You can use the returned value directly
another_result = add_numbers(10, 20) * 2
print(f"A different calculation result is: {another_result}")

# 7. Function with multiple parameters and a return
def calculate_area(length, width):
    """Calculates and returns the area of a rectangle."""
    area = length * width
    return area

area_of_box = calculate_area(5, 10)
print(f"\nThe area of the box is: {area_of_box}")
