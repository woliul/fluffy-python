# Day 5: User Input - Making Programs Interactive

# The input() function allows your program to take input directly from the user.
# When input() is called, the program pauses and waits for the user to type
# something and press Enter.

print("--- Personal Greeter ---")
# 1. Basic input: Getting a name
name = input("What's your name? ") # The text inside () is the prompt for the user
print(f"Hello, {name}! Nice to meet you.")

print("\n--- Simple Calculator ---")
# 2. Inputting numbers - IMPORTANT: input() always returns a STRING!
# If you want to do math, you MUST convert the string to a number (int or float).

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert strings to integers for calculation
num1 = int(num1_str)
num2 = int(num2_str)

sum_numbers = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_numbers}")

# Example with float conversion
price_str = input("Enter an item's price: ")
quantity_str = input("Enter the quantity: ")

price = float(price_str)
quantity = int(quantity_str)

total_cost = price * quantity
print(f"Total cost: ${total_cost:.2f}") # Formatted to 2 decimal places

print("\n--- Interactive Story ---")
# You can combine inputs to create simple interactive experiences
adjective = input("Give me an adjective: ")
noun = input("Give me a noun (plural): ")
verb = input("Give me a verb (past tense): ")

story = f"The {adjective} programmer saw some {noun} and {verb} with excitement!"
print(story)
