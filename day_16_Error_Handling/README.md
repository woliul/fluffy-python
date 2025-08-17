# Day 16: Error Handling - Writing Robust Code 🛡️

Welcome to Day 16! So far, we've learned to write code that works when everything goes as planned. Today, we're learning how to handle the unexpected. **Error handling** is the process of anticipating potential errors in your code and taking steps to prevent your program from crashing.

### What are Errors?

An **error** (or an **exception** in Python) is an event detected during program execution that disrupts the normal flow of the program. Common examples include:

* `ValueError`: Occurs when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert `"abc"` to an `int`).
* `ZeroDivisionError`: Occurs when you try to divide a number by zero.
* `FileNotFoundError`: Occurs when you try to open a file that does not exist.

### The `try...except` Block

The `try...except` block is the primary tool for handling errors in Python. It allows you to "try" a block of code, and if an exception occurs, the program "excepts" it and runs a different block of code gracefully instead of crashing.

* **`try`:** The code you suspect might cause an error is placed here.
* **`except`:** The code to run if a specific type of error occurs in the `try` block.
* **`else` (optional):** The code to run if the `try` block completes successfully with no errors.
* **`finally` (optional):** The code that will **always** run, regardless of whether an error occurred or not. It's often used for cleanup operations.

### 📝 Practice Exercises

1.  **Name & Age:** Ask the user for their name and age. Use a `try...except` block to ensure the age is a valid integer. If it's not, print a friendly error message and ask them to try again.
2.  **Simple Calculator:** Create a function that takes two numbers and an operation (`+`, `-`, `/`, `*`) as input. Use a `try...except` block to handle a `ZeroDivisionError` if the user tries to divide by zero.
3.  **File Reader:** Write a program that asks the user for a filename. Use a `try...except` block to handle a `FileNotFoundError` if the file doesn't exist.

### ✨ Best Practices & Professional Notes

* **Be Specific:** Always try to catch specific exceptions (e.g., `except ValueError`) instead of a generic `except`. This makes your code clearer and prevents you from hiding unexpected bugs.
* **Don't Hide Errors:** Error handling is for situations you can predict and handle gracefully. Do not use it to hide unexpected errors or poor coding logic.
* **Keep `try` Blocks Small:** The `try` block should contain as little code as possible to clearly isolate the part that might fail.
* **`finally` is for Cleanup:** Use the `finally` block to perform cleanup actions like closing a file or network connection, as it's guaranteed to run.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_16_Error_Handling` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_16_Error_Handling
    ```
3.  Run the script using:
    ```bash
    python error_handling_intro.py
    # Or if you installed python3:
    # python3 error_handling_intro.py
    ```

---

### ➡️ What's Next?

Tomorrow, on Day 17, we'll begin our introduction to **Object-Oriented Programming (OOP)**, a powerful paradigm for structuring and organizing code.

---

[⬅️ Back to Main Repository](../README.md)
