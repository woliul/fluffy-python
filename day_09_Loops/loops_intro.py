# Day 9: Loops - Automating Repetitive Tasks

# Loops allow you to execute a block of code multiple times.
# This is essential for processing lists, performing calculations, and more.

# 1. The `for` loop - iterating over a list
# Use 'for item in my_list:' to repeat an action for every item in a list.
fruits = ["apple", "banana", "cherry"]
print("--- For loop over a list ---")
for fruit in fruits:
    print(f"I like to eat a {fruit}.")

# 2. The `for` loop with `range()`
# The range() function generates a sequence of numbers.
# range(5) will generate 0, 1, 2, 3, 4.
print("\n--- For loop with range() ---")
for i in range(3):
    print(f"This is loop iteration {i + 1}.")

# range(start, stop)
print("\n--- For loop from 5 to 9 ---")
for num in range(5, 10):
    print(f"Number is: {num}")

# 3. The `while` loop - looping as long as a condition is True
# Be careful to avoid infinite loops! You must change the condition inside the loop.
print("\n--- While loop example ---")
counter = 0
while counter < 3:
    print(f"Counter is at: {counter}")
    counter += 1 # This is the crucial step to eventually stop the loop
