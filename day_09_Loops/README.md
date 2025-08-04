# Day 9: Loops - Automating Your Code 🔁

Welcome to Day 9! Yesterday, we learned about lists. Today, we're unlocking their true potential with **loops**! Loops are a fundamental programming concept that allows you to automate repetitive tasks, making your code efficient and scalable.

### What are Loops?

A loop is a control structure that executes a block of code repeatedly. Python has two primary types of loops: the `for` loop and the `while` loop.

### The `for` Loop: Iterating Over a Sequence

The `for` loop is used when you want to iterate over a sequence (like a list, string, or a range of numbers) and perform an action for each item. It's the most common type of loop you'll use.

* **Syntax:**
    ```python
    for item in sequence:
        # code to execute for each item
    ```
* **`range()` Function:** A helpful built-in function that generates a sequence of numbers.
    * `range(5)` -> generates numbers `0, 1, 2, 3, 4`.
    * `range(1, 5)` -> generates numbers `1, 2, 3, 4`.

### The `while` Loop: Repeating Until a Condition is False

The `while` loop executes a block of code as long as a specified condition is `True`. It's best used when you don't know in advance how many times the loop will run.

* **Syntax:**
    ```python
    while condition_is_True:
        # code to execute
        # make sure to change the condition to eventually stop the loop!
    ```
* **⚠️ Caution:** Be extremely careful with `while` loops! If the condition never becomes `False`, you will create an **infinite loop**, and your program will never stop.

### 📝 Practice Exercises

1.  **Print a List:** Create a list of your top 5 favorite movies. Use a `for` loop to print each movie title on a new line.
2.  **Countdown:** Use a `for` loop with the `range()` function to print a countdown from 5 to 1, followed by "Blastoff\!". (Hint: `range(5, 0, -1)`).
3.  **Simple Calculator:** Ask the user for a number. Use a `for` loop and `range()` to print the multiplication table for that number from 1 to 10 (e.g., `5 * 1 = 5`, `5 * 2 = 10`, etc.).
4.  **Interactive `while` loop:** Create a simple guessing game. Use a `while` loop to repeatedly ask the user for a number until they guess the correct number (you can hardcode the correct number).

### ✨ Best Practices & Professional Notes

  * **`for` vs. `while`:** Use a `for` loop when you know in advance how many times you want to loop (e.g., iterating over a list or a range of numbers). Use a `while` loop when the number of iterations is unknown and depends on a condition being met.
  * **Loop Control Statements:** Python offers `break` (to exit a loop prematurely) and `continue` (to skip the rest of the current iteration and go to the next one). We'll explore these more in future days\!
  * **Infinite Loops:** The single most common error with `while` loops is forgetting to include a statement that will eventually make the condition `False`. Always double-check this when writing `while` loops\!

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_09_Loops` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_09_Loops
    ```
3.  Run the script using:
    ```bash
    python loops_intro.py
    # Or if you installed python3:
    # python3 loops_intro.py
    ```

### ➡️ What's Next?

Tomorrow, we'll learn about **Functions** – how to create reusable blocks of code to keep your programs organized and efficient\!
