import requests

# Step 1: Define a class to model the data (OOP)
class Book:
    """A class to represent a book retrieved from an API."""
    def __init__(self, title, author, publish_date):
        self.title = title
        self.author = author
        self.publish_date = publish_date

    def display_info(self):
        """Prints the book's details in a user-friendly format."""
        print(f"\nTitle: {self.title}")
        print(f"Author(s): {', '.join(self.author)}")
        print(f"Published: {self.publish_date}")

# Step 2: Function to fetch data from an API and handle errors
def get_book_by_isbn(isbn):
    """
    Fetches book data from the Open Library API using an ISBN.
    
    This function uses:
    - `requests` to make an API call.
    - `try-except` for robust error handling.
    - A `dictionary` to parse the JSON response.
    """
    api_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    
    try:
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for bad status codes

        # Step 3: Parse the JSON response into a Python dictionary
        data = response.json()

        # Handle case where the ISBN is not found
        if not data:
            print(f"Error: No book found for ISBN {isbn}.")
            return None

        # Extract the relevant data from the dictionary
        book_info = data[f"ISBN:{isbn}"]
        title = book_info.get("title", "N/A")
        
        authors = [author.get("name", "Unknown") for author in book_info.get("authors", [])]
        
        publish_date = book_info.get("publish_date", "N/A")

        # Step 4: Create a Book object from the extracted data
        return Book(title, authors, publish_date)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None
    except KeyError:
        print(f"Error: Unexpected data format for ISBN {isbn}.")
        return None

# --- Main part of the script ---
if __name__ == "__main__":
    # Example usage with a valid ISBN
    valid_isbn = "9780545010221" # ISBN for Harry Potter and the Sorcerer's Stone
    book_object = get_book_by_isbn(valid_isbn)

    if book_object:
        book_object.display_info()
    
    # Example usage with an invalid ISBN to test error handling
    invalid_isbn = "0000000000000"
    get_book_by_isbn(invalid_isbn)
