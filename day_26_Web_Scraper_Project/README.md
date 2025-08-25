# Day 26: Project - Simple Web Scraper 🕸️

Today's project is a powerful one: you're building a **web scraper**. This program will autonomously browse the web, extract data, and save it for your use. It's a fundamental skill for data science and automation.

### What is Web Scraping?

Web scraping is the process of extracting information from websites. Think of it as a programmatically copying and pasting data from a web page.

### The Tools

* **`requests`:** This library is our workhorse for fetching the raw HTML content of a web page. It's like a delivery person bringing you a book from the internet.
* **`BeautifulSoup`:** This is our parser. It takes the raw, unstructured HTML and makes it easy to navigate and search for specific tags (like headings, links, or paragraphs). It's like an intelligent librarian who organizes the book's content so you can find exactly what you're looking for. 

[Image of a web scraper]


### Project Instructions

1.  **Installation:** Make sure you have the necessary libraries installed: `pip install requests beautifulsoup4`.
2.  **Fetch the Page:** Use `requests.get()` to download the HTML content.
3.  **Parse the HTML:** Use `BeautifulSoup(response.text, 'html.parser')` to create a `soup` object.
4.  **Find the Data:** Use methods like `soup.find_all()` to locate the data you want to extract.
5.  **Clean & Store:** Clean the extracted data (e.g., with `.strip()`) and save it to a file.
6.  **Error Handling:** Use `try...except` to make your scraper robust against network issues or non-existent pages.

### 📝 Practice Exercises

1.  **Extract All Links:** Modify the script to find and print all the hyperlinks (`<a>` tags) on the `example.com` page.
2.  **Scrape a Different Site:** Choose a simple, public website and try to scrape a different type of data, like a list of product names or article titles.
3.  **To-Do List Scraper:** Find a simple online to-do list example and scrape the items from it.

### ✨ Best Practices & Professional Notes

* **Be Respectful:** Always check a website's `robots.txt` file to see if scraping is allowed. Do not overload a server with too many requests too quickly.
* **Error Handling is Key:** Websites can change or go down. Robust error handling is crucial for any real-world scraper.
* **APIs First:** If a website has a public API, use it instead of scraping. It's more reliable and efficient.

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `day_26_Web_Scraper_Project` directory.
    ```bash
    cd path/to/your/fluffy-python/day_26_Web_Scraper_Project
    ```
3.  Run the script using:
    ```bash
    python web_scraper.py
    ```

---

### ➡️ What's Next?

Tomorrow, we'll continue our work with files by learning to read and write more structured data formats like **CSV** and **JSON**.

[⬅️ Back to Main Repository](./README.md)
