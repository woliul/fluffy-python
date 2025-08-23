# Day 25: More on Functions - *args & **kwargs

# --- Part 1: *args (Arbitrary Positional Arguments) ---
# The *args parameter collects all positional arguments into a tuple.
def sum_all_numbers(*args):
    """Calculates the sum of an arbitrary number of numbers."""
    print(f"args is a tuple: {args}")
    total = sum(args)
    print(f"The sum is: {total}")

print("--- Using *args ---")
sum_all_numbers(1, 2, 3)
sum_all_numbers(10, 20, 30, 40)
print("-" * 30)

# --- Part 2: **kwargs (Arbitrary Keyword Arguments) ---
# The **kwargs parameter collects all keyword arguments into a dictionary.
def create_profile(**kwargs):
    """Creates a user profile from an arbitrary number of key-value pairs."""
    print(f"kwargs is a dictionary: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key.capitalize()}: {value}")

print("--- Using **kwargs ---")
create_profile(name="Alice", age=30)
create_profile(username="coder_bob", city="New York", occupation="Developer")
print("-" * 30)

# --- Part 3: Combining *args and **kwargs ---
# They can be used together in the same function.
# The order is: regular arguments, *args, **kwargs
def combined_example(required_arg, *args, **kwargs):
    print(f"Required Argument: {required_arg}")
    print(f"Positional Arguments (*args): {args}")
    print(f"Keyword Arguments (**kwargs): {kwargs}")

print("--- Combining *args and **kwargs ---")
combined_example("I am required", 1, 2, 3, a=10, b=20)
