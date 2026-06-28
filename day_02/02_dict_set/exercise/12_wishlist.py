# TODO: Fill in the details of the item you plan to buy
order = [
    {"Name": "Car",
     "Brand": "Toyota",
     "Transmission": "Manual",
     "Info": "Brand new"}

     "Name"
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""

print("Order:")
for k, v in order.items():
    print(f"{k}: {v}")