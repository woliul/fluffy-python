
# Day 4: `Basic Operators`
> ### Your Code's Action Verbs `➕➖✖️➗`

Welcome to Day 4 of **Fluffy Python!** Today, we're diving into **operators** – the special symbols that tell Python to perform operations on values and variables. These are the "action verbs" of your code, allowing you to perform calculations, comparisons, and more!

### What are Operators?

Operators are symbols that carry out operations on operands (the values or variables they act upon). For example, in `5 + 3`, `+` is the operator and `5` and `3` are the operands.

Today, we're focusing on **Arithmetic Operators**, which are used for mathematical computations.

### Key Arithmetic Operators in Python

| Operator | Name             | Description                                              | Example           | Result |
| :------- | :--------------- | :------------------------------------------------------- | :---------------- | :----- |
| `+`      | Addition         | Adds two operands.                                       | `10 + 3`          | `13`   |
| `-`      | Subtraction      | Subtracts the right operand from the left.               | `10 - 3`          | `7`    |
| `*`      | Multiplication   | Multiplies two operands.                                 | `10 * 3`          | `30`   |
| `/`      | Division         | Divides the left operand by the right. **Always returns a float.** | `10 / 3`          | `3.33...`|
| `//`     | Floor Division   | Divides and returns the **integer part** of the quotient (removes the decimal). | `10 // 3`         | `3`    |
| `%`      | Modulo           | Divides and returns the **remainder** of the division.   | `10 % 3`          | `1`    |
| `**`     | Exponentiation   | Raises the left operand to the power of the right.       | `2 ** 3` (2^3)    | `8`    |


### 📝 Practice Exercises

1.  **BMI Calculator (Simplified):** Create variables for `weight_kg` and `height_m`. Calculate a simplified BMI using `BMI = weight_kg / (height_m ** 2)`. Print the result.
2.  **Minutes to Hours and Minutes:** You have `135` minutes. Use floor division (`//`) and modulo (`%`) to calculate how many full hours and how many remaining minutes that is. Print the result (e.g., "135 minutes is 2 hours and 15 minutes.").
3.  **Pizza Slices:** If you have `17` slices of pizza and `5` friends, how many slices does each friend get, and how many are left over for you? Use operators to figure this out and print the answer.
4.  **Cost Split:** Three people went out to dinner, and the total bill was `$85.75`. If they want to split it evenly, how much does each person pay? Use division.

### ✨ Best Practices & Professional Notes

  * **Operator Precedence (Order of Operations):** Remember PEMDAS/BODMAS from math class\! Python follows standard mathematical order: Parentheses first, then Exponentiation, Multiplication/Division/Modulo/Floor Division (from left to right), and finally Addition/Subtraction (from left to right). Use parentheses `()` to clarify or force a different order if needed.
      * Example: `10 + 5 * 2` is `20` (5\*2 then +10), not `30`. Use `(10 + 5) * 2` for 30.
  * **Assignment Operators:** Python also has shorthand assignment operators like `+=`, `-=`, `*=`, `/=`, etc.
      * `x = x + 5` can be written as `x += 5`. This is more concise and often preferred.
  * **Clarity over Cleverness:** While you *can* chain many operations, sometimes breaking complex calculations into smaller, well-named variable assignments makes your code much more readable and easier to debug.
  * **Division by Zero:** Be very careful with division (`/` or `//` or `%`)\! Dividing by zero will cause a `ZeroDivisionError`. In real applications, you'd add checks to prevent this.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_04_Operators` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_04_Operators
    ```
3.  Run the script using:
    ```bash
    python basic_operators.py
    # Or if you installed python3:
    # python3 basic_operators.py
    ```

### ➡️ What's Next?

Tomorrow, we'll learn about **User Input** – how to make your programs interactive and take information directly from the user!
