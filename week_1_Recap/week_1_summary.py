# Week 1 Recap: Putting It All Together!

# This simple script combines all the core concepts we learned in Week 1:
# print(), variables, data types, operators, and input().

# 1. User Input and Variables
print("Welcome to the Interactive Calculator!")
user_name = input("First, what's your name? ")

# 2. Input, Type Conversion (Casting), and Data Types
num1_str = input(f"Hello, {user_name}! Please enter the first number: ")
num2_str = input("Please enter the second number: ")

num1 = float(num1_str) # We'll use floats to allow for decimals
num2 = float(num2_str)

# 3. Arithmetic Operators
sum_result = num1 + num2
product_result = num1 * num2
is_positive = (sum_result > 0)

# 4. Conditional Statements
print("\n--- Results ---")
print(f"The sum is: {sum_result}")
print(f"The product is: {product_result}")

if is_positive:
    print("The sum of your numbers is a positive value.")
else:
    print("The sum of your numbers is a negative or zero value.")

# 5. Final Output
print("\nThank you for using the calculator!")