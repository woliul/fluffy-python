# Day 8: Lists - Storing Collections of Data

# A list is a fundamental data structure in Python. It's an ordered,
# changeable collection of items, and it allows for duplicate members.

# 1. Creating a list
# Lists are defined using square brackets []
fruits = ["apple", "banana", "cherry", "apple"]
numbers = [1, 5, 7, 9, 3]
print("My list of fruits:", fruits)
print("My list of numbers:", numbers)

# 2. Accessing list items by their index
# List items are indexed, starting from 0.
first_fruit = fruits[0]
third_fruit = fruits[2]
print(f"\nThe first fruit is: {first_fruit}") # Output: apple
print(f"The third fruit is: {third_fruit}") # Output: cherry

# You can also use negative indexing to start from the end
last_fruit = fruits[-1]
print(f"The last fruit is: {last_fruit}") # Output: apple

# 3. Getting the length of a list
# Use the len() function to find out how many items a list has.
num_fruits = len(fruits)
print(f"\nThere are {num_fruits} fruits in my list.")

# 4. Modifying a list (Lists are 'mutable')
# a) Change an item
fruits[1] = "blackberry"
print("\nFruits list after changing the second item:", fruits)

# b) Add an item to the end
fruits.append("orange")
print("Fruits list after appending 'orange':", fruits)

# c) Remove an item
fruits.remove("apple") # Removes the first occurrence
print("Fruits list after removing 'apple':", fruits)

# d) Add an item at a specific index
fruits.insert(1, "grape")
print("Fruits list after inserting 'grape' at index 1:", fruits)
