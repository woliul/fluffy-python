# Day 20: Working with APIs 🌐

Welcome to Day 20! Today, you're learning one of the most exciting skills in modern programming: how to use **APIs (Application Programming Interfaces)**. APIs allow your programs to communicate with other software applications and services over the internet.

### What are APIs? The Waiter Analogy

Imagine you're at a restaurant. You don't go into the kitchen to make your food. Instead, you tell the **waiter** what you want. The waiter takes your order to the kitchen and then brings back your food.

* **You (the client):** Your Python program.
* **The waiter (the API):** The messenger that takes your request and brings back the response.
* **The kitchen (the server):** The online service or database that processes your request.

### Key Concepts

* **Requests:** Your program makes a "request" to the API. The most common method is `GET`, used to retrieve data.
* **Responses:** The API sends back a "response" containing the data you asked for.
* **JSON (JavaScript Object Notation):** The most popular format for APIs to send and receive data. It looks very similar to a Python dictionary. The `requests` library automatically converts this to a Python dictionary.
* **The `requests` Library:** This is the standard in Python for making HTTP requests. You must install it first: `pip install requests`.

### 📝 Practice Exercises

1.  **Star Wars API:** Use the `requests` library to get data about a Star Wars character. The API URL is `https://swapi.dev/api/people/1/`. Print the character's name and homeworld.
2.  **Weather App:** Find a free weather API and sign up for a key. Write a program that asks the user for a city name and then fetches the current temperature for that city.

### ✨ Best Practices & Professional Notes

* **Check Status Codes:** Always check the response's `status_code` to ensure the request was successful. A `200 OK` means everything is good.
* **Use `try...except`:** Working with APIs involves network requests that can fail. Always use a `try...except` block to handle potential errors.
* **API Documentation:** Every API has documentation that explains how to use it. Always read the docs!

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_20_APIs` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_20_APIs
    ```
3.  Install the necessary library:
    ```bash
    pip install requests
    ```
4.  Run the script using:
    ```bash
    python api_intro.py
    ```

---

### ➡️ What's Next?

Tomorrow is Day 21! We'll celebrate a full three weeks of learning with a **Week 3 Recap**, bringing everything together from our OOP and API lessons.

[⬅️ Back to Main Repository](../README.md)
