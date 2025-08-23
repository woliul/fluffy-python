# Day 24: Lambda Functions & List Comprehensions

# --- Part 1: List Comprehensions ---

# The traditional way to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = []
for x in numbers:
    squares.append(x**2)
print(f"Squares (traditional for loop): {squares}")

# The Pythonic way: using a List Comprehension
squares_comp = [x**2 for x in numbers]
print(f"Squares (list comprehension):   {squares_comp}")

# List comprehension with a conditional filter
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

print("-" * 30)

# --- Part 2: Lambda Functions ---

# A simple lambda function to add two numbers
add = lambda a, b: a + b
print(f"Lambda function result (5 + 3): {add(5, 3)}")

# Lambda functions are most useful with higher-order functions like 'sorted', 'map', and 'filter'

# Sorting a list of tuples by the second element using a lambda
my_list = [(1, 5), (3, 2), (2, 8)]
# The lambda function defines the sort key (x[1] refers to the second element)
sorted_list = sorted(my_list, key=lambda x: x[1])
print(f"Sorted list by second element: {sorted_list}")

# Using a lambda function with 'map' to apply a function to every item
fahrenheit_temps = [32, 68, 86, 104]
# Convert to Celsius: (f - 32) * 5/9
celsius_temps = list(map(lambda f: (f - 32) * 5/9, fahrenheit_temps))
print(f"Temperatures in Celsius: {celsius_temps}")

# Using a lambda function with 'filter' to select items that meet a condition
numbers_to_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_to_filter))
print(f"Filtered even numbers: {even_numbers}")
