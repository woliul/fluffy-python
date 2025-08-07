# Day 10: Functions - Your First Reusable Code Blocks 🧱

Welcome to Day 10! Today, we're making a huge leap in coding maturity by learning about **Functions**. A function is a block of code that only runs when it's called. They are essential for organizing your code, making it readable, and preventing you from repeating the same instructions over and over again.

### What is a Function?

Think of a function as a mini-program within your main program. It's a named, reusable sequence of instructions that you can execute whenever you need to.

### Key Concepts

1.  **Defining a Function:**
    * You define a function using the `def` keyword, followed by the function's name and parentheses.
    * The code inside the function must be indented.
    * A docstring (the triple-quoted string `"""..."""`) is a good practice to describe what the function does.

    ```python
    def my_function(parameter1, parameter2):
        """This is a docstring explaining the function."""
        # Code goes here
    ```

2.  **Calling a Function:**
    * To execute the code in a function, you must "call" it by its name, followed by parentheses.

    ```python
    my_function("value1", "value2") # Calling the function
    ```

3.  **Parameters and Arguments:**
    * **Parameters:** The variables listed inside the parentheses when you *define* the function (e.g., `parameter1`).
    * **Arguments:** The actual values you pass into the function when you *call* it (e.g., `"value1"`).

4.  **The `return` Statement:**
    * A function doesn't have to just `print()`. It can also send a value back to the caller using the `return` keyword.
    * Once a `return` statement is executed, the function stops, and the returned value can be stored in a variable.

### Code Example: `functions_intro.py`

```python
# Day 10: Functions - Reusable Blocks of Code

# Functions are blocks of code that perform a specific task.
# They help organize your code and make it reusable.

# 1. Defining a simple function with no parameters
def say_hello():
    """This function simply prints a greeting."""
    print("Hello, Python learner!")

# 2. Calling the function
# To run the code inside the function, you must call it by its name.
print("Calling the function for the first time:")
say_hello()

print("\nCalling it again:")
say_hello()

# 3. Defining a function with parameters
# Parameters are variables that the function accepts as input.
def greet_user(name):
    """This function greets a user by their name."""
    print(f"Hello, {name}! Welcome to Day 10.")

# 4. Calling the function with an argument
# 'Alice' is the argument passed to the 'name' parameter.
print("\nCalling greet_user with a name:")
greet_user("Alice")
greet_user("Woliul")

# 5. A function that returns a value
# The 'return' keyword sends a value back to the caller.
def add_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    sum_result = a + b
    return sum_result

# 6. Using the returned value
print("\nCalling add_numbers:")
result = add_numbers(5, 7)
print(f"The result of adding 5 and 7 is: {result}")

# You can use the returned value directly
another_result = add_numbers(10, 20) * 2
print(f"A different calculation result is: {another_result}")

# 7. Function with multiple parameters and a return
def calculate_area(length, width):
    """Calculates and returns the area of a rectangle."""
    area = length * width
    return area

area_of_box = calculate_area(5, 10)
print(f"\nThe area of the box is: {area_of_box}")
````

### 📝 Practice Exercises

1.  **Simple Greeting Function:** Create a function called `welcome_message` that takes one parameter `user_name` and prints a personalized welcome message.
2.  **Number Square:** Create a function `square_number` that takes a number as a parameter, calculates its square, and `return`s the result. Store the returned value in a variable and print it.
3.  **Temperature Converter Function:** From Day 5, you asked for a temperature. Now, wrap that logic in a function called `celsius_to_fahrenheit`. It should take one parameter `celsius` and `return` the converted temperature. (`F = C * 9/5 + 32`).
4.  **List Processor:** Create a function `print_list` that takes a list as a parameter and uses a `for` loop (from Day 9) to print each item in the list.

### ✨ Best Practices & Professional Notes

  * **Naming Conventions:** Function names should be descriptive, lowercase, and use underscores (`snake_case`), just like variables.
  * **Docstrings:** The triple-quoted string right after the `def` line is called a "docstring." It's a standard practice for explaining what your function does, its parameters, and what it returns. This makes your code self-documenting.
  * **Scope:** Variables created inside a function are local to that function and cannot be accessed from outside. This is a good thing\! It prevents accidental conflicts and makes your code more modular.
  * **Functions are First-Class Objects:** In Python, functions can be assigned to variables, passed as arguments to other functions, and returned from functions. This is a more advanced concept, but it's good to know early on.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_10_Functions` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_10_Functions
    ```
3.  Run the script using:
    ```bash
    python functions_intro.py
    # Or if you installed python3:
    # python3 functions_intro.py
    ```
--

### ➡️ What's Next?

Tomorrow, we'll learn how to extend the power of our programs by using **Modules and Libraries** – other people's code\!

