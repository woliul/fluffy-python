# Day 22: Tuples & Sets 🗂️

Welcome to Week 4! We're starting with two more versatile data structures: **Tuples** and **Sets**. While lists and dictionaries are great all-purpose tools, Tuples and Sets solve specific problems more elegantly and efficiently.

### Key Concepts

#### Tuples
Think of a **tuple** as an immutable list—a collection of items that, once created, **cannot be changed**. They are **ordered**, meaning elements have a defined position.

* **Key Feature:** Immutability. This makes them useful for data that should be constant, like a point on a graph or the dimensions of an image. It also makes them faster to process than lists.
* **Syntax:** Defined using parentheses `()`.

#### Sets
A **set** is a collection of items that are **unordered** and **do not allow duplicate elements**. 

[Image of a Venn Diagram with Union, Intersection, and Difference]
 This makes them ideal for tasks involving uniqueness and set logic.

* **Key Feature:** Uniqueness. If you convert a list to a set, all duplicate elements are automatically removed. They also provide extremely fast membership testing (`if item in my_set`).
* **Syntax:** Defined using curly braces `{}`.

### 📝 Practice Exercises

1.  **Find the Unique Vowels:** Given a string, use a set to find all the unique vowels in it.
2.  **Combine Data:** You have two lists of students who attended two different events. Use set operations to find:
    * Students who attended **both** events.
    * Students who attended **only one** of the events.
3.  **Tuple to List:** Create a tuple of your favorite movies. Convert it to a list, add a new movie, and then convert it back to a tuple.

### ✨ Best Practices & Professional Notes

* **Use Tuples for Fixed Data:** If you have data that shouldn't change, like a database record or configuration values, a tuple is a safer and more memory-efficient choice than a list.
* **Use Sets for Uniqueness:** Sets are the fastest way to check for membership and eliminate duplicates. Don't use them for data that needs to be in a specific order.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `day_22_Tuples_&_Sets` directory.
    ```bash
    cd path/to/your/fluffy-python/day_22_Tuples_&_Sets
    ```
3.  Run the script using:
    ```bash
    python tuples_sets_intro.py
    ```

---

### ➡️ What's Next?

Tomorrow, we will explore advanced string manipulation and a powerful tool called **Regular Expressions** to find and match text patterns.

[⬅️ Back to Main Repository](./README.md)
