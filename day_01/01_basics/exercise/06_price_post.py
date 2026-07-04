# Price notification template
price_notification = "The price of {} is ${}."

# TODO: Post: Latte ($3.5)
item1 = "Latte"
price1 = 3.5
print(price_notification.format(item1, price1))
print(f"{item1} {price1}")

# TODO: Post: Espresso ($2.75)
item2 = "Espresso"
price2 = 2.75
print(price_notification.format(item2, price2))

# TODO: Post: Cappuccino ($4.0)
item3 = "Cappuccino"
price3 = 4.0
print(price_notification.format(item3, price3))

total = price1 + price2 + price3
print("Total payment: $",total)