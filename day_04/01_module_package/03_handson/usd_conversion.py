import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

# Get the latest conversion rate from USD to PHP
conversion = response.json()
print(conversion)
print(conversion['rates']['PHP'])
print()
