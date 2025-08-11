# Day 12: Project Day - An Interactive Quiz Game 🎮

Welcome to Day 12 and the first project of our journey! Today, we're not just learning a new concept—we're applying everything we've covered so far to build a complete, working program: an **Interactive Quiz Game**.

This project will help you see how all the building blocks (variables, lists, loops, functions, and modules) come together to create something meaningful.

### Project Breakdown

Our quiz game uses several key concepts:

1.  **Lists:** We use a list to store all the quiz questions and their corresponding answers. Each question itself is a list containing the question text, a list of options, and the correct answer.
2.  **Functions:** The entire game logic is wrapped inside a single function, `run_quiz()`. This makes our code organized and easy to run.
3.  **Loops (`for` loop):** A `for` loop iterates through our list of questions, ensuring we ask every single one.
4.  **`input()` and Conditional Statements (`if/else`):** We use `input()` to get the user's answer, and then an `if/else` statement to check if the answer is correct and provide instant feedback.
5.  **Modules (`random`):** We import the `random` module to shuffle the questions, making the quiz different every time you play.
6.  **Variables & Operators:** Variables are used to keep track of the user's score, and operators are used to check for equality (`==`) and increment the score (`score += 1`).

### Practice Exercises

**Enhance the Quiz Game:**

1.  **Add more questions:** Expand the `quiz_questions` list with 5-10 new questions on any topic you like.
2.  **Add a welcome message:** Before the quiz starts, add a `print()` statement to greet the user and explain the rules.
3.  **Validate user input:** What if the user types an answer other than A, B, C, or D? Use a `while` loop to repeatedly ask for input until they provide a valid answer. (Hint: `while user_answer not in ["A", "B", "C", "D"]:`)
4.  **Give final feedback:** After printing the final score, use `if/elif/else` statements to print a different message based on how well they did (e.g., "Great job!", "You can do better!").

### ✨ Best Practices & Professional Notes

* **Modular Code:** Breaking your code into functions, even in a small program, makes it easier to read, test, and debug.
* **Data Structures:** Organizing your data in a clear structure (like our list of lists) is a crucial step in programming.
* **Comments & Docstrings:** Comments and docstrings are incredibly important in projects. They help you remember what your code does and help others understand it.
* **Leverage Libraries:** We used the `random` module to get powerful functionality (shuffling) with a single line of code. This is a core principle of efficient programming.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_12_Quiz_Project` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_12_Quiz_Project
    ```
3.  Run the script using:
    ```bash
    python interactive_quiz.py
    # Or if you installed python3:
    # python3 interactive_quiz.py
    ```

### ➡️ What's Next?

Tomorrow, on Day 13, we'll learn about **File I/O** (Input/Output) – how to read and write data to and from external files!
