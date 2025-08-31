# Part 2: Basic Data Exploration

import pandas as pd

file_path = 'sample_data.csv'

try:
    df = pd.read_csv(file_path)
    
    # Check the first 5 rows of the DataFrame
    print("First 5 rows:")
    print(df.head())
    
    # Get a summary of the DataFrame (data types, non-null counts, etc.)
    print("\nDataFrame info:")
    df.info()
    
    # Get descriptive statistics for numerical columns
    print("\nDescriptive statistics:")
    print(df.describe())
    
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
