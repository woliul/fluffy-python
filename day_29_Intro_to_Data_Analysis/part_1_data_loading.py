# Part 1: Loading Data with pandas

# You need to install pandas first: pip install pandas
import pandas as pd

# The name of the CSV file. Make sure it's in the same directory.
file_path = 'sample_data.csv'

# Read the CSV file into a pandas DataFrame
# A DataFrame is like a spreadsheet or SQL table.
try:
    df = pd.read_csv(file_path)
    print("DataFrame loaded successfully:")
    print(df)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
