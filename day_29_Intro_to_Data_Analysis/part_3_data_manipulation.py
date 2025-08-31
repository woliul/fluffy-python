# Part 3: Simple Data Manipulation

import pandas as pd

file_path = 'sample_data.csv'

try:
    df = pd.read_csv(file_path)
    print("Original DataFrame:")
    print(df)
    
    # Filter the DataFrame to show only sales in 'New York'
    ny_sales = df[df['City'] == 'New York']
    print("\nSales in New York:")
    print(ny_sales)
    
    # Sort the DataFrame by the 'Sales' column in descending order
    sorted_df = df.sort_values(by='Sales', ascending=False)
    print("\nDataFrame sorted by Sales:")
    print(sorted_df)
    
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
