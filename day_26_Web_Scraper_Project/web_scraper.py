# Day 26: Project - Simple Web Scraper

# We'll use 'requests' to get the HTML and 'BeautifulSoup' to parse it.
import requests
from bs4 import BeautifulSoup

def simple_scraper(url):
    """Scrapes all the headings from a given URL."""
    try:
        # Step 1: Fetch the HTML content
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Step 2: Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 3: Find and extract all h1, h2, and h3 headings
        headings = soup.find_all(['h1', 'h2', 'h3'])
        
        # Step 4: Process and store the extracted data
        extracted_data = [heading.get_text().strip() for heading in headings]

        # Step 5: Save the data to a file
        with open("scraped_headings.txt", "w", encoding="utf-8") as file:
            for item in extracted_data:
                file.write(item + "\n")
        
        print("Scraping successful! Headings saved to scraped_headings.txt")
        return extracted_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# The website to scrape
target_url = "https://example.com"
scraped_headings = simple_scraper(target_url)

if scraped_headings:
    print("\nExtracted Headings:")
    for heading in scraped_headings:
        print(f"- {heading}")
