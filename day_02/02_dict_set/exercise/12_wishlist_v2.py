# TODO: Fill in the details of the items you plan to buy
wishlist = [
    {"Name": "Car",
     "Brand": "Toyota",
     "Transmission": "Manual",
     "Info": "Brand new"},
    {"Name": "Laptop",
     "Brand": "Dell",
     "Info": "Brand new"},
]


# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
for order in wishlist:
    print("Wishlist:")
    for k, v in order.items():
        print(f"{k}: {v}")
    print()