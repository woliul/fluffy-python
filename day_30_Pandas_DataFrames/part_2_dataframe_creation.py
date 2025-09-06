# Part 2: Creating DataFrames

import pandas as pd

# Example 1: Creating a DataFrame from a dictionary of lists
# This is a common way to create a DataFrame column by column
data_dict = {
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [1200, 25, 75],
    'Quantity': [10, 50, 30]
}
df_from_dict = pd.DataFrame(data_dict)
print("DataFrame created from a dictionary of lists:")
print(df_from_dict)

# Example 2: Creating a DataFrame from a list of dictionaries
# This is useful when your data is organized row by row (e.g., from a JSON file)
data_list_of_dicts = [
    {'Product': 'Monitor', 'Price': 300, 'Quantity': 8},
    {'Product': 'Webcam', 'Price': 50, 'Quantity': 20}
]
df_from_list = pd.DataFrame(data_list_of_dicts)
print("\nDataFrame created from a list of dictionaries:")
print(df_from_list)
