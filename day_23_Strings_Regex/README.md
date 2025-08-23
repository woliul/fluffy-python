# Day 23: More on Strings & Regular Expressions 🔍

Today is all about mastering text manipulation, a vital skill for web scraping, data cleaning, and log file analysis. We'll explore advanced built-in string methods and then unlock the true power of text with **Regular Expressions (Regex)**.

### Key Concepts

#### Advanced String Methods
Python's `str` class has many useful methods. Today, we focus on a few that are essential for cleaning and preparing text data:
* `.strip()`: Removes leading and trailing whitespace.
* `.replace(old, new)`: Replaces all occurrences of a substring.
* `.split(delimiter)`: Splits a string into a list based on a delimiter.
* `.join(iterable)`: Joins elements of an iterable into a single string.

#### Regular Expressions (Regex)
Regular expressions are a powerful language for defining and matching text patterns. Think of it as a super-advanced search tool. Instead of searching for a literal string, you can search for a *pattern* like "a three-digit number," "an email address," or "a word followed by a comma." 

* **The `re` Module:** Python's built-in library for working with regex.
* **Patterns:** You write a special string (a pattern) to describe the text you're looking for. Common symbols include:
    * `.`: Any single character.
    * `\d`: A digit (`0-9`).
    * `\w`: A word character (`a-z`, `A-Z`, `0-9`, `_`).
    * `+`: Matches one or more of the preceding character.
    * `*`: Matches zero or more of the preceding character.
* **Functions:**
    * `re.search(pattern, string)`: Finds the first match for a pattern.
    * `re.findall(pattern, string)`: Finds all non-overlapping matches and returns them as a list.

### 📝 Practice Exercises

1.  **Extract Usernames:** Use a regular expression to extract all usernames (the part before the `@`) from a list of email addresses.
2.  **Phone Number Validator:** Write a function that uses a regular expression to check if a string is a valid phone number in the format `XXX-XXX-XXXX`.
3.  **Clean & Format:** Take a messy string with multiple spaces and leading/trailing whitespace. Use a combination of `.strip()` and `.join()` to format it into a single, clean sentence with single spaces between words.

### ✨ Best Practices & Professional Notes

* **Start Simple:** If a basic string method works, use it! Only reach for regex when the pattern is too complex for simple methods.
* **Use Raw Strings:** Always prefix your regex pattern string with `r` (e.g., `r'\d+'`). This creates a "raw string," preventing Python from interpreting special characters like `\n` or `\t`.
* **Regex Testers:** Use online tools like `regex101.com` to build and test your patterns before putting them in your code.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `day_23_Strings_&_Regex` directory.
    ```bash
    cd path/to/your/fluffy-python/day_23_Strings_&_Regex
    ```
3.  Run the script using:
    ```bash
    python strings_regex_intro.py
    ```

---

### ➡️ What's Next?

Tomorrow, we will explore powerful one-line Python statements with **Lambda Functions** and **List Comprehensions**.

[⬅️ Back to Main Repository](./README.md)
