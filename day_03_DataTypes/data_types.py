# Day 3: Data Types in Detail & Checking Types

# Understanding data types is crucial because different operations
# can be performed on different types of data.
# Python is dynamically typed, meaning it automatically assigns the type,
# but knowing the type helps prevent errors and write correct logic.

# 1. Integers (int): Whole numbers, positive or negative, without decimals.
product_count = 100
customer_id = 12345
year = 2025
print(f"Product Count: {product_count}, Type: {type(product_count)}")
print(f"Customer ID: {customer_id}, Type: {type(customer_id)}")

# 2. Floats (float): Numbers with a decimal point, positive or negative.
temperature = 25.5
exchange_rate = 110.75
pi_value = 3.14159
print(f"Temperature: {temperature}, Type: {type(temperature)}")
print(f"Exchange Rate: {exchange_rate}, Type: {type(exchange_rate)}")

# 3. Strings (str): Sequences of characters (text). Enclosed in single or double quotes.
user_name = "Alice Smith"
greeting = 'Hello, world!'
address = "123 Python St."
print(f"User Name: {user_name}, Type: {type(user_name)}")
print(f"Greeting: {greeting}, Type: {type(greeting)}")

# 4. Booleans (bool): Represents truth values - True or False.
#    Used for conditional logic.
is_admin = True
has_discount = False
is_logged_in = True
print(f"Is Admin: {is_admin}, Type: {type(is_admin)}")
print(f"Has Discount: {has_discount}, Type: {type(has_discount)}")

# Why knowing types matters:
# Try adding a number and a string directly - it will cause an error!
# current_year = 2025
# message = "The year is " + current_year # This would cause a TypeError
# print(message)

# You often need to convert types (Type Casting)
current_year = 2025
message = "The year is " + str(current_year) # Convert int to string for concatenation
print(message)

# Converting string to integer or float for calculations
str_number_int = "123"
str_number_float = "45.67"
int_value = int(str_number_int)
float_value = float(str_number_float)
print(f"Converted Integer: {int_value}, Type: {type(int_value)}")
print(f"Converted Float: {float_value}, Type: {type(float_value)}")
