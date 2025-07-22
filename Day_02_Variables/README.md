# Day 2: Variables - Your Data Containers 📦

Welcome to `Day 2` of my **Fluffy Python** learning journey! Today, we're diving into **variables** – a fundamental concept in programming that allows you to store and manage data within your programs. Think of them as labeled containers or named storage locations in your computer's memory.

### What are Variables?

Variables hold values that can change throughout your program's execution. They allow you to:

* **Store Information:** Like names, ages, prices, or true/false states.
* **Reuse Data:** Use the same piece of information multiple times without retyping it.
* **Make Code Flexible:** Change values easily without modifying the core logic.

### Basic Data Types

Python automatically determines the type of data you store in a variable, but it's good to know the common ones:

* **String (`str`):** Used for text. Enclosed in single or double quotes (e.g., `"hello"`, `'world'`).
* **Integer (`int`):** Whole numbers (e.g., `10`, `-50`, `1000`).
* **Float (`float`):** Numbers with decimal points (e.g., `3.14`, `2.5`, `-0.01`).
* **Boolean (`bool`):** Represents truth values: `True` or `False`. (Note the capital T and F).

### Code Example: `variables_intro.py`

Here's the code we're exploring today. You'll find this in the `variables_intro.py` file within this directory.

```python
# Day 2: Variables - Storing Information

# Variables are like labeled boxes where you can store different types of data.
# You give the box a name, and then you put something inside it.

# 1. Storing a String (text)
user_name = "Woliul"
greeting = 'Hello, Python Learner!'
print("User Name:", user_name)
print("Greeting:", greeting)

# 2. Storing an Integer (whole number)
age = 30
number_of_lessons = 2
print("Age:", age)
print("Lessons completed:", number_of_lessons)

# 3. Storing a Float (decimal number)
price = 19.99
pi_value = 3.14159
print("Product Price:", price)
print("Value of Pi:", pi_value)

# 4. Storing a Boolean (True/False value)
is_learning_python = True
has_finished_course = False
print("Is learning Python?", is_learning_python)
print("Has finished course?", has_finished_course)

# You can also change the value of a variable
current_mood = "Happy"
print("Current mood (before change):", current_mood)
current_mood = "Excited about Python!"
print("Current mood (after change):", current_mood)

# Variables can be used in calculations
total_cost = price * number_of_lessons
print("Total cost of lessons:", total_cost)
````

### 📝 Practice Exercises

Ready to get hands-on with variables? Try these:

1.  **Your Profile:** Create variables to store your city, your favorite hobby, and whether you own a pet (True/False). Then, print them out with descriptive labels.
2.  **Simple Inventory:** Imagine you're tracking items. Create variables for `item_name` (string), `item_quantity` (integer), and `item_price_per_unit` (float). Calculate and print the `total_item_value`.
3.  **Dynamic Greeting:** Ask the user for their name (using `input()`, which we'll cover more tomorrow, but you can try it\!) and store it in a variable. Then, print a personalized greeting like "Hello, [Name]\!".
4.  **Update a Variable:** Create a variable called `score` with an initial value. Then, change its value a couple of times (e.g., `score = score + 10`) and print its value after each change.

### ✨ Best Practices & Professional Notes

  * **Naming Conventions:**
      * **Descriptive Names:** Use clear, descriptive names for your variables (e.g., `user_name` instead of `un`). This makes your code much easier to read and understand.
      * **Lowercase with Underscores:** The common Python convention for variable names is `snake_case` (all lowercase, words separated by underscores).
      * **Avoid Keywords:** Don't use Python's reserved keywords (like `print`, `if`, `for`, `True`, `False`) as variable names.
  * **Dynamic Typing:** Python is "dynamically typed," meaning you don't need to explicitly declare a variable's type (like `int user_age;`). Python figures it out based on the value you assign. This makes coding faster but requires you to be aware of the data type when performing operations (e.g., you can't add a string and a number directly).
  * **Type Checking (Advanced):** For more complex projects, Python offers `type hints` (e.g., `user_name: str = "Alice"`) to help tools check for potential type errors, though this doesn't change runtime behavior.

### 🏃 How to Run This Code

If you've followed the [Setup guide](../README.md), you can run this code:

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_02_Variables` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_02_Variables
    ```
3.  Run the script using:
    ```bash
    python variables_intro.py
    # Or if you installed python3:
    # python3 variables_intro.py
    ```

### ➡️ What's Next?

Tomorrow, we'll dive deeper into **Data Types** and learn how to check the type of a variable and why it matters!
