# Part 1: Introduction to Series

import pandas as pd

# Example 1: Creating a Series from a list
# The index is automatically generated (0, 1, 2...)
data_list = [10, 20, 30, 40]
series_a = pd.Series(data_list)
print("Series from a list:")
print(series_a)

# Example 2: Creating a Series from a dictionary
# The dictionary keys become the index
data_dict = {'New York': 150, 'Los Angeles': 50, 'Chicago': 250}
series_b = pd.Series(data_dict)
print("\nSeries from a dictionary:")
print(series_b)

# Example 3: Accessing elements
print(f"\nValue at position 1 (list series): {series_a[1]}")
print(f"Value for 'Chicago' (dict series): {series_b['Chicago']}")
