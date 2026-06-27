# TODO: Ask the user for an input that should be a number
from enum import nonmember


def get_number_input():
    number = int(input("Enter a number: "))

    try:
        number_converted = int(number)
        if number_converted < 0:
            raise ValueError ()

        return number_converted
    except ValueError:
        print("Number is not valid!")

    return None

def get_safe_number_input():
    number = get_number_input()
    while not number:
        number = get_number_input()

    return number

var = get_number_input()

get_safe_number_input()

# TODO: Then try to convert this into an integer using the following:
#number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case

# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry
