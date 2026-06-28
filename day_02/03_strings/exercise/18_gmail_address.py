# Ask the user for an input
email_input = input("Enter your email address: ")

valid_email = email_input.endswith("@gmail.com")
if valid_email:
    print("This is a valid gmail address")
else:
    print("This is NOT a valid gmail address")
