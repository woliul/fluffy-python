# Day 23: More on Strings & Regular Expressions

# We'll use the built-in 're' module for regular expressions.
import re

# --- Part 1: Advanced String Methods ---
text = "  Hello,    Python! This is a test string.  "

# Strip leading/trailing whitespace
stripped_text = text.strip()
print(f"Stripped text: '{stripped_text}'")

# Replace a substring
replaced_text = stripped_text.replace("Python", "World")
print(f"Replaced text: '{replaced_text}'")

# Split a string into a list
words = replaced_text.split()
print(f"Split into words: {words}")

# Join a list of strings back into a single string
joined_text = "-".join(words)
print(f"Joined text: '{joined_text}'")

print("-" * 30)

# --- Part 2: Regular Expressions (Regex) ---

# A simple string containing an email and phone number
sample_text = "My email is test.user@email.com and my phone number is 123-456-7890."

# Regex Pattern 1: Find an email address
# \w+ matches one or more word characters (letters, numbers, underscore)
# \. matches a literal dot
# @ matches a literal @
# [A-Za-z.]+ matches one or more letters or dots
email_pattern = r'\w+\.[A-Za-z0-9_.]+@[A-Za-z.]+\.[A-Za-z.]+'

# Use re.search() to find the first match
email_match = re.search(email_pattern, sample_text)
if email_match:
    print(f"Found email: {email_match.group()}")

# Regex Pattern 2: Find a phone number
# \d{3} matches exactly 3 digits
# - matches a literal hyphen
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_match = re.search(phone_pattern, sample_text)
if phone_match:
    print(f"Found phone number: {phone_match.group()}")

# Regex Pattern 3: Find all numbers
all_numbers_pattern = r'\d+'
all_numbers_list = re.findall(all_numbers_pattern, sample_text)
print(f"Found all numbers: {all_numbers_list}")
