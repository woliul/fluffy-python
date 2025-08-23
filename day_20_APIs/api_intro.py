# Day 20: APIs - Getting Data from the Web

# The 'requests' library is the standard for making HTTP requests in Python.
# If you haven't installed it, run 'pip install requests' in your terminal.
import requests

def get_a_joke():
    """Fetches a random joke from a public API."""
    api_url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # The response.json() method converts the JSON content to a Python dictionary
        joke_data = response.json()
        
        setup = joke_data["setup"]
        punchline = joke_data["punchline"]
        
        print(f"Joke Setup: {setup}")
        print(f"Punchline: {punchline}")
            
    except requests.exceptions.RequestException as e:
        # Handle network errors, connection problems, etc.
        print(f"An error occurred: {e}")

# Call the function to run the program
get_a_joke()
