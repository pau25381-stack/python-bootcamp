# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
}

# TODO: Print the country for the given country code
# TODO: # If the key is not found, print Unknown
print(country_codes.get(input("Enter country code: "), "UNKNOWN"))