# Week 4 Recap Challenge: Scrape, Clean, and Store Links

import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_unique_links(url):
    """
    Scrapes all unique links from a given URL, cleans them, and stores them in a list of dictionaries.
    
    This script combines skills from Week 4:
    - Requests for API/Web Scraping (Day 26)
    - Sets for ensuring uniqueness (Day 22)
    - Regular Expressions for cleaning data (Day 23)
    - JSON for structured data storage (Day 27)
    """
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Use a Set to automatically handle unique links
        unique_links = set()
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # Use Regex to clean the link (remove leading/trailing slashes, etc.)
                cleaned_link = re.sub(r'^/|/$', '', href).strip()
                if cleaned_link:
                    unique_links.add(cleaned_link)

        # Create a list of dictionaries for JSON
        structured_data = [{"link": link} for link in sorted(list(unique_links))]

        # Save the data to a JSON file
        with open("unique_links.json", "w", indent=4) as f:
            json.dump(structured_data, f)

        print("\nSuccessfully scraped unique links and saved to unique_links.json!")
        return structured_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Run the scraper
scrape_unique_links("http://example.com")
