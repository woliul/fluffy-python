# Day 4: Basic Operators - Performing Calculations

# Operators are special symbols that perform operations on values and variables.
# Today, we're focusing on Arithmetic Operators, used for mathematical calculations.

# Let's define two numbers to work with
num1 = 15
num2 = 4

print(f"Numbers: num1 = {num1}, num2 = {num2}\n") # Adding a newline for readability

# 1. Addition (+)
sum_result = num1 + num2
print(f"Addition ({num1} + {num2}): {sum_result}") # Output: 19

# 2. Subtraction (-)
difference = num1 - num2
print(f"Subtraction ({num1} - {num2}): {difference}") # Output: 11

# 3. Multiplication (*)
product = num1 * num2
print(f"Multiplication ({num1} * {num2}): {product}") # Output: 60

# 4. Division (/) - Always returns a float (decimal number)
quotient_float = num1 / num2
print(f"Division ({num1} / {num2}): {quotient_float}") # Output: 3.75

# 5. Floor Division (//) - Returns the integer part of the division (no remainder)
quotient_integer = num1 // num2
print(f"Floor Division ({num1} // {num2}): {quotient_integer}") # Output: 3

# 6. Modulo (%) - Returns the remainder of the division
remainder = num1 % num2
print(f"Modulo ({num1} % {num2}): {remainder}") # Output: 3 (15 divided by 4 is 3 with a remainder of 3)

# 7. Exponentiation (**) - Raises the first number to the power of the second
power_result = num1 ** num2 # 15 to the power of 4 (15 * 15 * 15 * 15)
print(f"Exponentiation ({num1} ** {num2}): {power_result}") # Output: 50625

print("\n--- Practical Examples ---")

# Example: Calculate total price with discount
item_price = 25.50
quantity = 3
discount_percent = 0.10 # 10%
subtotal = item_price * quantity
discount_amount = subtotal * discount_percent
final_price = subtotal - discount_amount
print(f"Subtotal: ${subtotal:.2f}") # Formatted to 2 decimal places
print(f"Discount: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")

# Example: Check if a number is even or odd using modulo
check_num = 7
if check_num % 2 == 0:
    print(f"{check_num} is an even number.")
else:
    print(f"{check_num} is an odd number.")
