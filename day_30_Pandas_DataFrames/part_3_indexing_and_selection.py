# Part 3: Indexing and Selection

import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'New York']
}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4'])
print("Original DataFrame:")
print(df)

# Example 1: Selecting a single column using bracket notation
ages = df['Age']
print("\nSelected 'Age' column:")
print(ages)

# Example 2: Selecting multiple columns
name_city = df[['Name', 'City']]
print("\nSelected 'Name' and 'City' columns:")
print(name_city)

# Example 3: Using .loc[] for label-based selection
# Select a single row by its label
row_2_loc = df.loc['row2']
print("\nRow selected by label 'row2' using .loc[]:")
print(row_2_loc)

# Select a specific value by row and column labels
age_loc = df.loc['row3', 'Age']
print(f"\nAge of 'row3' using .loc[]: {age_loc}")

# Example 4: Using .iloc[] for integer-based selection
# Select the first row
row_0_iloc = df.iloc[0]
print("\nFirst row selected using .iloc[]:")
print(row_0_iloc)

# Select the value at the first row and second column (Age)
age_iloc = df.iloc[0, 1]
print(f"\nValue at position (0, 1) using .iloc[]: {age_iloc}")
