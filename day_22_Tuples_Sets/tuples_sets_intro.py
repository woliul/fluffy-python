# Day 22: Tuples & Sets

# --- Tuples ---
# Tuples are ordered, immutable collections. They are useful for data that should not change.
print("--- Tuples ---")
coordinates = (10, 20)
print(f"Original tuple: {coordinates}")

# You can access elements by index, just like lists.
print(f"First coordinate: {coordinates[0]}")

# Trying to change a tuple will result in a TypeError.
try:
    coordinates[0] = 5
except TypeError as e:
    print(f"Error: {e}")

# Tuples can contain different data types.
mixed_tuple = ("hello", 3.14, True)
print(f"Mixed tuple: {mixed_tuple}")

print("-" * 20)

# --- Sets ---
# Sets are unordered, mutable collections of unique elements.
print("--- Sets ---")
my_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Original list with duplicates: {my_list}")

# You can easily remove duplicates by converting a list to a set.
unique_numbers = set(my_list)
print(f"Set of unique numbers: {unique_numbers}")

# You can add or remove elements from a set.
unique_numbers.add(6)
unique_numbers.remove(1)
print(f"Set after adding 6 and removing 1: {unique_numbers}")

# Set operations are very efficient.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: Elements in either set.
print(f"Union of A and B: {set_a.union(set_b)}") # or set_a | set_b

# Intersection: Elements in both sets.
print(f"Intersection of A and B: {set_a.intersection(set_b)}") # or set_a & set_b

# Difference: Elements in A but not B.
print(f"Difference of A and B: {set_a.difference(set_b)}") # or set_a - set_b
