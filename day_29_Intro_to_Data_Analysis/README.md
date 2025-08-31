# Week 5 # Day 29: Intro to Data Analysis 📊

Welcome to Week 5! We are officially starting our specialization in **Data Analysis**. This week, you will learn the core libraries that turn Python into a powerful tool for working with data. Today, we begin with an introduction to the data analysis workflow and the most important library of all: **`pandas`**.

### Details Introduction

Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making. It's how we turn raw numbers into actionable insights. While you could do this with core Python lists and dictionaries, it would be slow and difficult. The `pandas` library provides a high-performance, easy-to-use data structure that makes data manipulation a breeze.

### Key Concepts

* **The Data Analysis Workflow:** A typical workflow involves several steps:
    1.  **Collection:** Gathering data from various sources (files, databases, APIs).
    2.  **Cleaning:** Handling missing values, removing duplicates, and correcting errors.
    3.  **Exploration:** Gaining an initial understanding of the data through summaries and visualizations.
    4.  **Analysis:** Applying statistical methods to find patterns and relationships.

* **Introducing `pandas`:** The `pandas` library is the cornerstone of data analysis in Python. It provides two primary data structures:
    1.  **Series:** A one-dimensional array-like object that can hold any data type. Think of it as a single column from an Excel spreadsheet.
    2.  **DataFrame:** A two-dimensional, table-like data structure with labeled axes (rows and columns). This is the most used `pandas` object, as it is intuitive and mirrors a spreadsheet or a SQL table. 

* **Fundamental Operations:** With `pandas`, basic operations become simple one-liners:
    1.  **Loading Data:** You can load data from many formats (CSV, Excel, JSON) directly into a DataFrame.
    2.  **Inspecting Data:** Functions like `.head()`, `.tail()`, and `.info()` let you quickly inspect your data to ensure it loaded correctly and to check its structure.
    3.  **Descriptive Statistics:** The `.describe()` method provides a quick summary of numerical data, including count, mean, standard deviation, and quartiles.

### 📝 Practice Exercises

1.  Open the `sample_data.csv` file and manually inspect it. Then, load it into a pandas DataFrame using `part_1_data_loading.py`.
2.  Using `part_2_data_exploration.py`, explore the DataFrame. Find out how many non-null entries there are in each column and get the average value for the `Sales` column.
3.  Modify `part_3_data_manipulation.py` to filter the data to only include products with sales greater than 200.

### ✨ Best Practices & Professional Notes

* **Always Inspect Your Data:** Never assume your data loaded correctly. Always use `.info()`, `.head()`, and `.describe()` immediately after loading to check for issues like missing values or incorrect data types.
* **The "Dirty Data" Problem:** In real-world projects, data is rarely clean. A significant portion of a data analyst's job is dedicated to the cleaning and preparation stage.
* **Use `pandas` for Tabular Data:** If your data can be represented in a table, `pandas` is almost always the right tool for the job. Avoid manual loops for data manipulation as `pandas` operations are highly optimized and much faster.

### 🏃 How to Run This Code

1.  First, make sure you have the `pandas` library installed by running:
    ```bash
    pip install pandas
    ```
2.  Save the provided CSV data (see the code files) as `sample_data.csv` in the same directory.
3.  Run each Python file from your terminal to see its output:
    ```bash
    python part_1_data_loading.py
    python part_2_data_exploration.py
    python part_3_data_manipulation.py
    ```

---

[⬅️ Back to Main Repository](./README.md)
