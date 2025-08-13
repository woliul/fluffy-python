# Day 15: Data Structures - Dictionaries 📖

Welcome to Week 3! Today, we're learning about a new data structure that's fundamental to Python: the **Dictionary**. While lists are great for ordered collections, dictionaries are perfect for storing data in a more descriptive way using **key-value pairs**.

### What are Dictionaries?

A dictionary is an unordered, changeable collection of items. Think of it like a real-world dictionary or a phone book where you look up a "word" (the **key**) to find its "definition" (the **value**).

* **Syntax:** Defined with curly braces `{}`.
* **Key-Value Pairs:** Each item consists of a unique `key` followed by a `value`. The key and value are separated by a colon (`:`).
* **Keys:** Must be unique and immutable (like strings, numbers, or tuples).
* **Values:** Can be anything, including other lists or dictionaries.

### Key Operations

1.  **Creating a Dictionary:**
    ```python
    my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    ```
2.  **Accessing Items:** Use the key inside square brackets.
    ```python
    car_brand = my_dict["brand"]
    # or a safer way to avoid errors if the key doesn't exist:
    car_model = my_dict.get("model")
    ```
3.  **Adding/Modifying Items:** Assign a value to a new or existing key.
    ```python
    my_dict["color"] = "red"  # Adds a new key-value pair
    my_dict["year"] = 2021   # Updates the value for an existing key
    ```
4.  **Removing Items:** Use the `del` keyword or the `.pop()` method.
    ```python
    del my_dict["model"]
    ```

### 📝 Practice Exercises

1.  **Create a Profile:** Create a dictionary called `user_profile` with keys for `"username"`, `"email"`, and `"is_active"`.
2.  **Access and Update:** Print the username and then update the `"is_active"` status to `True`.
3.  **Looping:** Use a `for` loop to iterate through your `user_profile` dictionary and print each `key` and `value`.
4.  **Phone Book:** Create a dictionary of contacts. Ask the user for a name, then print their phone number from the dictionary. What happens if the name isn't in your dictionary?

### ✨ Best Practices & Professional Notes

* **Use Descriptive Keys:** Keys should be meaningful strings that clearly describe the data they hold.
* **`.get()` vs. `[]`:** When accessing a key, `my_dict.get('key')` is generally safer than `my_dict['key']` because if the key doesn't exist, `.get()` returns `None` instead of raising an error. This is especially useful when you're not sure if a key exists.
* **Checking for Keys:** To check if a key exists in a dictionary, use the `in` keyword: `if "key" in my_dict:`. This is a very common and efficient operation.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_15_Dictionaries` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_15_Dictionaries
    ```
3.  Run the script using:
    ```bash
    python dictionaries_intro.py
    # Or if you installed python3:
    # python3 dictionaries_intro.py
    ```

### ➡️ What's Next?

Tomorrow, on Day 16, we'll learn about **Error Handling** with `try...except`, which will make our programs more robust and user-friendly!

[⬅️ Back to Main Repository](../README.md)
