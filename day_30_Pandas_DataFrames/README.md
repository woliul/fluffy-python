# Week 5 # Day 30: pandas - DataFrames & Series 🐼

Today, we get to the heart of the `pandas` library by exploring its two core data structures: **Series** and **DataFrame**. Understanding these foundational components is crucial for becoming proficient in data analysis and manipulation.

### Details Introduction

While we saw how to load data into a DataFrame yesterday, today we will learn how to create these objects from scratch and, more importantly, how to efficiently access and select the data they contain. Mastering these concepts will allow you to slice, dice, and transform your datasets with precision and confidence.

### Key Concepts

* **The `Series` Object:** A `Series` is a one-dimensional, labeled array. It is similar to a Python list or a `numpy` array but comes with an explicit index, which can be an integer, a string, or any other hashable type. Think of it as a single column of data from a spreadsheet, complete with row labels.

    * **Example 1:** Creating a Series from a list of values.
    * **Example 2:** Creating a Series from a dictionary, where the keys automatically become the index.
    * **Example 3:** Accessing elements by both their position and their label.

* **The `DataFrame` Object:** A `DataFrame` is a two-dimensional, labeled data structure with columns that can hold different data types. It is the most common `pandas` object and is analogous to a spreadsheet or a SQL table. 

    * **Example 1:** Creating a DataFrame from a dictionary of lists (column-oriented data).
    * **Example 2:** Creating a DataFrame from a list of dictionaries (row-oriented data, often from JSON or APIs).
    * **Example 3:** Performing basic operations like checking the DataFrame's shape (`.shape`) and columns (`.columns`).

* **Indexing and Selection:** This is a vital skill for working with DataFrames. `pandas` provides powerful and flexible ways to select specific rows and columns.
    * **`[]` (Bracket Notation):** Used for selecting columns (e.g., `df['column_name']`).
    * **`.loc[]` (Label-based Indexing):** The primary method for selecting data by its explicit label. You can select rows, columns, or both using their names/labels.
    * **`.iloc[]` (Integer-based Indexing):** The method for selecting data by its integer position (index). This works just like standard Python list indexing.

### 📝 Practice Exercises

1.  Create a DataFrame with columns for `Product`, `Price`, and `Quantity`. Populate it with at least 5 rows of data.
2.  Using the DataFrame you created, use `.loc[]` to select and print only the rows where the product is a "Laptop" or "Monitor".
3.  Use `.iloc[]` to select and print the `Price` and `Quantity` columns for the first two rows of your DataFrame.

### ✨ Best Practices & Professional Notes

* **Explicit is Better:** While `df['col']` is a common shortcut for selecting a column, always use `.loc[]` or `.iloc[]` when selecting rows and columns simultaneously. This prevents **chained indexing warnings** (`SettingWithCopyWarning`) and makes your code more readable.
* **Vectorization:** `pandas` operations are "vectorized," meaning they are optimized to operate on entire Series or DataFrames at once, without a `for` loop. This is much faster and more efficient.
* **Data Consistency:** Always ensure your data types are correct using `df.info()`. Incorrect data types can lead to unexpected errors in calculations.

### 🏃 How to Run This Code

1.  First, ensure you have `pandas` installed:
    ```bash
    pip install pandas
    ```
2.  Save each Python file in the directory.
3.  Run them from your terminal to see the output:
    ```bash
    python part_1_series_intro.py
    python part_2_dataframe_creation.py
    python part_3_indexing_and_selection.py
    ```

---

[⬅️ Back to Main Repository](./README.md)
