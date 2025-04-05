# 05 April 2025

# Greeting with Customization:
# 1. Write a program that asks the user for their first name and last name separately.
# 2. Store these names in two different variables.
# 3. Print a greeting that combines their first and last name, such as "Hello, [First Name] [Last Name]!".

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")

# Using string concatenation
print("Hello, " + first_name + " " + last_name + "!")

# Using f-string
print(f"Hello, {first_name} {last_name}!")
