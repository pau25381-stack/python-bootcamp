# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
correct_user = username_input == correct_username
correct_pass = password_input == correct_password
correct_credentials = correct_user and correct_pass

admin_user = username_input == admin_username
admin_pass = password_input == admin_password
correct_admin = admin_user and admin_pass

if correct_credentials or correct_admin:
    print("Access Granted")
else:
    print("Access Denied")


