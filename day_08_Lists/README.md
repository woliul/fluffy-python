
# Day 8: Data Structures - Mastering Lists 📋

Welcome to Day 8 and the start of Week 2! We're leveling up from single variables to our first **data structure**: the **List**. A list is a powerful and versatile tool for storing collections of data, and you will use it constantly in your Python programs.

### What is a List?

A list is an ordered, changeable collection of items. Think of it as a single variable that can hold a whole sequence of values.

* **Defined by:** Square brackets `[]`.
* **Items:** Can be of any data type (`str`, `int`, `float`, `bool`, or even other lists!).
* **Ordered:** The items have a defined order, which you can access using an `index`.
* **Changeable (Mutable):** You can add, remove, and change items in a list after it has been created.

### Key Concepts & Operations

1.  **Creating a List:**
    ```python
    my_shopping_list = ["milk", "bread", "eggs"]
    my_numbers = [1, 2, 3, 4, 5]
    ```

2.  **Indexing:**
    * Lists are zero-indexed, meaning the first item is at index `0`.
    * `my_list[0]` gives you the first item.
    * `my_list[-1]` gives you the last item.

3.  **Common Methods:**
    * `.append(item)`: Adds an item to the end of the list.
    * `.remove(item)`: Removes the first occurrence of the specified item.
    * `.insert(index, item)`: Adds an item at a specific index.
    * `len(my_list)`: A built-in function that returns the number of items in the list.

### Code Example: `data_structures_lists.py`

```python
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
````

### 📝 Practice Exercises

1.  **Shopping List:** Create a list of your favorite foods. Print the first and last items.
2.  **Add & Remove:** Create an empty list called `my_tasks`. Use `.append()` to add three tasks. Then, use `.remove()` to remove one of them. Print the list after each step.
3.  **Guest List:** Start with a list of three guests for a party. Use `print()` to announce that one guest can't make it. Then, use `.remove()` and `.append()` to replace them with a new guest. Print the final guest list.
4.  **Count Items:** Create a list with some duplicate numbers or words. Use `len()` to print how many items are in the list.

### ✨ Best Practices & Professional Notes

  * **Zero-Indexing is Standard:** The concept of starting at `0` is fundamental in programming, not just for lists but also for strings and other data structures. It's a key habit to build.
  * **Mutability:** Be aware that because lists are mutable, if you assign `list_b = list_a`, both variables actually point to the same list in memory. Changing `list_b` will also change `list_a`. If you want a separate copy, use `list_b = list_a.copy()`.
  * **Heterogeneous Data:** While lists can hold different data types, it's often a best practice to keep a list's contents homogeneous (all numbers, all strings, etc.) for clarity and easier processing.
  * **Looping (Coming Soon\!):** The real power of lists is when you combine them with loops (`for` and `while`) to process every item in the list automatically. We'll cover this tomorrow\!

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_08_Lists` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_08_Lists
    ```
3.  Run the script using:
    ```bash
    python data_structures_lists.py
    # Or if you installed python3:
    # python3 data_structures_lists.py
    ```

### ➡️ What's Next?

Tomorrow, we'll learn about **Loops** – how to automatically repeat actions on every item in our lists\!
