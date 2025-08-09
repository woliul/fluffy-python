# Day 11: Modules & Libraries - Borrowing Pre-written Code

# A module is a Python file with functions and variables that you can use.
# A library is a collection of related modules.

# 1. Importing a built-in module
# The 'import' statement brings the module into your program's scope.
import math

# Now you can use functions and variables from the 'math' module.
# You must use the module name followed by a dot (e.g., math.pi).
print("--- Using the 'math' module ---")
print(f"The value of Pi is: {math.pi}")
print(f"The square root of 64 is: {math.sqrt(64)}")
print(f"10 raised to the power of 3 is: {math.pow(10, 3)}")


# 2. Importing another useful built-in module: `random`
import random

print("\n--- Using the 'random' module ---")
# randint(a, b) generates a random integer between a and b (inclusive)
random_number = random.randint(1, 100)
print(f"Here's a random number between 1 and 100: {random_number}")

# choice(sequence) picks a random item from a list
outcomes = ["Win", "Lose", "Draw"]
random_outcome = random.choice(outcomes)
print(f"The outcome of your game is: {random_outcome}")

# 3. Importing a specific function from a module
# Use 'from module import function' to import only what you need.
from random import shuffle

print("\n--- Using 'from ... import ...' ---")
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")
shuffle(my_list) # Now we can use shuffle() directly without 'random.shuffle()'
print(f"Shuffled list: {my_list}")

# 4. Giving an imported module an alias
import random as r

print("\n--- Using an alias ('as r') ---")
print(f"Another random number: {r.randint(10, 20)}")
