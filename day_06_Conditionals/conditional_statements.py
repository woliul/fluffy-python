# Day 6: Conditional Statements - Making Decisions

# Conditional statements allow your program to make decisions and
# execute different code blocks based on whether a condition is True or False.

# 1. The 'if' statement
# Executes code ONLY if the condition is True.

temperature = 28
if temperature > 25:
    print("It's a hot day!")

# 2. The 'if-else' statement
# Executes one block if the condition is True, and another if False.

age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3. The 'if-elif-else' statement
# Checks multiple conditions in order. 'elif' (else if) for additional checks.

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80: # This runs only if score < 90
    print("Grade: B")
elif score >= 70: # This runs only if score < 80
    print("Grade: C")
else: # This runs if none of the above conditions were True
    print("Grade: F")

# 4. Using input() with conditionals
# Remember input() returns a string, so convert it if needed for comparison!

user_num_str = input("Enter a number: ")
user_num = int(user_num_str) # Convert input to an integer

if user_num % 2 == 0: # Check if the number is even (remainder when divided by 2 is 0)
    print(f"The number {user_num} is even.")
else:
    print(f"The number {user_num} is odd.")

# 5. Combining conditions (Logical Operators - brief intro for awareness)
# 'and', 'or', 'not' are used to combine multiple conditions.
is_sunny = True
is_warm = False
if is_sunny and is_warm: # Both must be True
    print("Perfect beach weather!")
elif is_sunny or is_warm: # At least one must be True
    print("Good weather for a walk.")
else:
    print("Stay indoors.")
