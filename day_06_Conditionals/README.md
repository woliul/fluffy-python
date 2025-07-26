# Day 6: `Conditional Statements` - Guiding Your Code's Decisions

Welcome to Day 6 of **Fluffy Python!** Today, your programs are getting smarter. We're introducing **Conditional Statements**, which allow your Python code to make decisions and execute different sets of instructions based on whether certain conditions are met. This is fundamental for building dynamic and responsive applications!

### What are Conditional Statements?

At their core, conditional statements are about "if this, then that, else do something else." They control the **flow of execution** in your program.

### Key Statements: `if`, `elif`, `else`

1.  **`if` Statement:**
    * The most basic conditional. The code block directly indented underneath `if` will only execute if its condition evaluates to `True`.
    * Syntax:
        ```python
        if condition:
            # code to execute if condition is True
        ```

2.  **`else` Statement:**
    * Provides an alternative path. The code block under `else` will execute if the `if` condition (and any preceding `elif` conditions) are all `False`.
    * Syntax:
        ```python
        if condition:
            # code if True
        else:
            # code if False
        ```

3.  **`elif` (Else If) Statement:**
    * Used when you have multiple conditions to check, one after another. `elif` conditions are only checked if all previous `if` and `elif` conditions were `False`.
    * Syntax:
        ```python
        if first_condition:
            # code if first_condition is True
        elif second_condition: # Only checked if first_condition was False
            # code if second_condition is True
        else: # Only executed if all above conditions were False
            # code if all conditions were False
        ```

### Comparison Operators

These are the operators you use to form the `conditions` that evaluate to `True` or `False`:

* `==` : Equal to
* `!=` : Not equal to
* `>`  : Greater than
* `<`  : Less than
* `>=` : Greater than or equal to
* `<=` : Less than or equal to

### ⚠️ Crucial: Indentation is Key!

Python uses **indentation** (typically 4 spaces) to define code blocks. The code lines belonging to an `if`, `elif`, or `else` statement *must* be indented. If you get it wrong, Python will throw an `IndentationError`!

### 📝 Practice Exercises

1.  **Voting Eligibility:** Ask the user for their age. Using `if/else`, print "You are eligible to vote\!" if they are 18 or older, otherwise print "You are not yet eligible to vote."
2.  **Traffic Light:** Create a variable `light_color` (e.g., "red", "yellow", "green"). Use `if-elif-else` to print appropriate actions ("Stop", "Slow down", "Go").
3.  **Positive, Negative, or Zero:** Ask the user for a number. Use `if-elif-else` to determine if the number is positive, negative, or zero.
4.  **Password Check (Simple):** Create a variable `correct_password = "password123"`. Ask the user to `input()` a password. Use `if/else` to print "Access Granted\!" or "Access Denied." (Note: This is a very insecure method for real passwords, but good for practice\!).

### ✨ Best Practices & Professional Notes

  * **Readability:** Keep your conditions clear and simple. If a condition becomes too long or complex, consider breaking it down into smaller, readable parts or using helper functions (future topic\!).
  * **"Dangling Else"**: Python's indentation solves the "dangling else" problem (where it's unclear which `if` an `else` belongs to in nested conditionals), making your code clearer.
  * **Boolean Zen:** When a condition is already a boolean variable (e.g., `is_active = True`), you don't need `if is_active == True:`. Just `if is_active:` is perfectly fine and more Pythonic. Similarly, `if not is_active:` for `if is_active == False:`.
  * **Logical Operators (`and`, `or`, `not`):** These allow you to combine multiple conditions (as briefly shown in the example). `and` means both sides must be true; `or` means at least one side must be true; `not` negates a condition.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_06_Conditionals` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_06_Conditionals
    ```
3.  Run the script using:
    ```bash
    python conditional_statements.py
    # Or if you installed python3:
    # python3 conditional_statements.py
    ```

### ➡️ What's Next?

Tomorrow is **Day 7!** We'll celebrate completing Week 1 with a self-reflection and a look at our progress. Get ready to celebrate your first week of consistent learning!
