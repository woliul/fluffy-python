# Day 16: Error Handling - Making Your Code Robust

# Error handling allows a program to deal with unexpected situations gracefully,
# without crashing. We use the 'try...except' block for this.

# 1. A program without error handling (will crash)
print("--- Program without error handling ---")
# This code will crash if the user enters a non-numeric value
# try:
#     age = int(input("Enter your age: "))
#     print(f"You will be {age + 1} next year.")
# except ValueError:
#     print("Invalid input. Please enter a number.")


# 2. A program with basic error handling
print("\n--- Program with basic error handling ---")
try:
    age = int(input("Enter your age: "))
    print(f"You will be {age + 1} next year.")
except ValueError:
    # This code runs only if a ValueError occurs in the 'try' block
    print("Invalid input! Please enter a number.")


# 3. Handling multiple types of errors
print("\n--- Handling multiple error types ---")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Error: Please enter only numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# 4. Using 'else' and 'finally'
print("\n--- The 'else' and 'finally' blocks ---")
try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("That's not a number.")
else:
    # This code runs only if the 'try' block is successful
    print(f"The number you entered is {user_input}.")
finally:
    # This code always runs, whether an error occurred or not
    print("Exiting the program.")
