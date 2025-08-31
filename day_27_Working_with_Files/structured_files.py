# Day 27: Working with Structured Files - CSV & JSON

# We use Python's built-in modules for this. No installation needed!
import csv
import json

# --- Part 1: Working with CSV (Comma-Separated Values) ---
print("--- CSV Operations ---")

# Data to be written to a CSV file
csv_data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London'],
    ['Charlie', '35', 'Paris']
]

# Writing to a CSV file
# 'w' mode opens the file for writing. newline='' prevents extra blank rows.
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print("data.csv created successfully.")

# Reading from a CSV file
print("Reading from data.csv:")
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("-" * 25)

# --- Part 2: Working with JSON (JavaScript Object Notation) ---
print("--- JSON Operations ---")

# Data to be written to a JSON file
json_data = {
    "name": "Jane Doe",
    "age": 42,
    "is_student": False,
    "courses": ["Python", "Data Science", "Web Development"]
}

# Writing to a JSON file
# 'w' mode opens the file for writing. indent=4 makes it human-readable.
with open('data.json', 'w') as file:
    json.dump(json_data, file, indent=4)
print("data.json created successfully.")

# Reading from a JSON file
print("Reading from data.json:")
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# You can access JSON data just like a Python dictionary
print(f"Name from JSON: {loaded_data['name']}")
