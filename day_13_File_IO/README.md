# Day 13: File I/O - Saving Your Program's Data 💾

Welcome to Day 13! Today we're learning a crucial skill that allows our programs to remember things: **File I/O (Input/Output)**. File I/O is how a program reads information from a file and writes information to a file, making data persistent even after the program has finished running.

### Key Concepts

* **Opening Files:** You interact with files using Python's built-in `open()` function. You must specify the file's name and the mode you want to open it in.
* **File Modes:**
    * `'r'` (Read): Opens a file for reading. This is the default.
    * `'w'` (Write): Opens a file for writing. **Warning**: This mode will overwrite any existing content in the file.
    * `'a'` (Append): Opens a file for writing, but adds new content to the end of the file.
* **The `with` Statement:** The most reliable way to handle files. The `with open(...) as file:` syntax ensures that the file is automatically closed when you're done with it, even if an error occurs. This prevents potential data corruption and memory leaks.
* **Reading Content:**
    * `file.read()`: Reads the entire file content into a single string.
    * `file.readline()`: Reads a single line from the file.
    * `file.readlines()`: Reads all lines and returns them as a list of strings.
* **Writing Content:**
    * `file.write("string")`: Writes a string to the file. You must manually add `\n` for a new line.

### 📝 Practice Exercises

1.  **To-Do List:** Write a program that uses `input()` to ask the user for a new to-do list item. Use `'a'` mode to append this item to a file named `todo.txt`.
2.  **Read and Display:** Write a program that reads the entire content of a text file (e.g., `todo.txt` from the previous exercise) and prints it line by line using a `for` loop.
3.  **Create a Log File:** Write a function that takes a message as an argument and appends it, along with the current time (you'll need to import the `datetime` module for this!), to a file named `log.txt`.

### ✨ Best Practices & Professional Notes

* **Always Use `with`:** The `with open(...)` statement is considered a best practice in Python. It's safer and cleaner than manually calling `file.close()`.
* **Handle File Not Found:** What if a file doesn't exist? Reading a non-existent file will cause a `FileNotFoundError`. A professional program would use a `try...except` block to gracefully handle this. (We'll cover this in a future lesson!)
* **File Paths:** For this simple example, we're using files in the same directory. In real-world applications, you'll work with full file paths to specify locations on your computer.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_13_File_IO` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_13_File_IO
    ```
3.  Run the script using:
    ```bash
    python file_io_intro.py
    # Or if you installed python3:
    # python3 file_io_intro.py
    ```

### ➡️ What's Next?

Tomorrow is Day 14! We'll celebrate another week of learning with a **Week 2 Recap Article**, reviewing all the amazing progress we've made.
