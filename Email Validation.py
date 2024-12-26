import re

# Input: Get the email address from the user
email = input("Enter an email address to validate: ")

# Define the regular expression for a valid email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validate the email
if re.match(email_pattern, email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
