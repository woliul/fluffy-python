# Week 2 Recap: A Simple "To-Do List" Program

import os  # A module for interacting with the operating system

# 1. Functions & Data Structures (Lists)
def display_list(items):
    """Prints out the items in a list."""
    if not items:
        print("Your to-do list is empty.")
    else:
        print("--- Your To-Do List ---")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")
        print("-----------------------")

# 2. File I/O (Reading & Writing)
def load_list():
    """Loads a list from a file if it exists, otherwise returns an empty list."""
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_list(items):
    """Saves a list of items to a file."""
    with open("todo.txt", "w") as file:
        for item in items:
            file.write(item + "\n")

# Main program logic
todo_list = load_list()

while True:
    display_list(todo_list)
    print("\nOptions: add, remove, exit")
    user_choice = input("Enter your choice: ").lower()

    if user_choice == "add":
        new_item = input("Enter a new to-do item: ")
        todo_list.append(new_item)
        save_list(todo_list)
    elif user_choice == "remove":
        if todo_list:
            try:
                item_num = int(input("Enter the number of the item to remove: "))
                if 1 <= item_num <= len(todo_list):
                    removed_item = todo_list.pop(item_num - 1)
                    print(f"Removed '{removed_item}'.")
                    save_list(todo_list)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
    elif user_choice == "exit":
        print("Goodbye! Your list has been saved.")
        break
    else:
        print("Invalid choice. Please try again.")
