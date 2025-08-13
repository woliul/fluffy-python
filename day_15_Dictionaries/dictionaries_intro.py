# Day 15: Dictionaries - Key-Value Pairs

# A dictionary is an unordered, changeable, and indexed collection.
# It stores data in key: value pairs.

# 1. Creating a dictionary
# Dictionaries are defined with curly braces {}.
person = {
    "name": "Woliul",
    "age": 30,
    "is_student": False,
    "courses": ["Python", "Data Science"]
}

# 2. Accessing items
# You access a dictionary item by referring to its key.
name = person["name"]
age = person.get("age")  # The .get() method is safer
print(f"The person's name is: {name}")
print(f"The person's age is: {age}")

# 3. Modifying items
# You can change the value of a specific key.
person["age"] = 31
print(f"The person's new age is: {person['age']}")

# 4. Adding a new item
# Adding a new key-value pair is simple.
person["city"] = "Dhaka"
print(f"The person now lives in: {person['city']}")
print("Updated dictionary:", person)

# 5. Removing an item
# Use the del keyword or the .pop() method.
del person["is_student"]
print("Dictionary after removing 'is_student':", person)

# 6. Looping through a dictionary
# You can loop through keys, values, or both.
print("\n--- Looping through keys ---")
for key in person.keys():
    print(key)

print("\n--- Looping through values ---")
for value in person.values():
    print(value)

print("\n--- Looping through both keys and values ---")
for key, value in person.items():
    print(f"{key}: {value}")
