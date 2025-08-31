# Day 27: Working with Structured Files: CSV & JSON 📂

Today, you're learning how to read and write two of the most common file formats for structured data: **CSV** and **JSON**. These formats are the language of data exchange, used everywhere from spreadsheets to web APIs.

### Key Concepts

#### CSV (Comma-Separated Values)
A CSV file is a simple, plain-text format for storing data in a table-like structure. Each line of the file represents a data record, and each field is separated by a comma. It's a universal standard for sharing data between spreadsheets and databases. 

* **Python Module:** The built-in `csv` module.
* **Key Functions:** `csv.reader()` to read data and `csv.writer()` to write data.

#### JSON (JavaScript Object Notation)
JSON is a lightweight, human-readable data format that's a direct reflection of a Python dictionary. It is the go-to format for transferring data on the web, especially with APIs.

* **Python Module:** The built-in `json` module.
* **Key Functions:** `json.load()` to read a file and `json.dump()` to write to one.

### 📝 Practice Exercises

1.  **JSON to CSV Converter:** Write a script that reads the `data.json` file you created and writes the data to a new CSV file.
2.  **Add a New Record:** Read the `data.csv` file, append a new row of data to it, and then write the updated content back to the file.
3.  **Handle Nested JSON:** Create a more complex dictionary with nested lists or dictionaries and then write it to a JSON file.

### ✨ Best Practices & Professional Notes

* **Use `with open()`:** Always use the `with open(...)` statement when working with files. It ensures the file is automatically closed, even if an error occurs.
* **Built-in is Best:** Python's standard library modules (`csv` and `json`) are highly optimized and should be your first choice for handling these file types.
* **Understand Data Structure:** Before you start reading or writing, have a clear idea of the data's structure (what are the columns in a CSV, what are the keys in a JSON?).

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `day_27_Working_with_Files` directory.
    ```bash
    cd path/to/your/fluffy-python/day_27_Working_with_Files
    ```
3.  Run the script using:
    ```bash
    python structured_files.py
    ```

### ➡️ What's Next?

Tomorrow is Day 28, which means it's time for our **Week 4 Recap**! We'll review everything we've learned, from tuples and sets to web scraping and structured files.

[⬅️ Back to Main Repository](./README.md)
