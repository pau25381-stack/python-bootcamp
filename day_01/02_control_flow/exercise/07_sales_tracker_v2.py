# TODO: Ask the user how many items will be calculated
input_count = 2
total = 0

# TODO: Use a for loop to ask for more than one cost and count

for i in range(input_count):
    item_cost = int(input("Enter the cost:"))  # Let the user enter a number
    item_count = int(input("Number of items:"))  # Let the user enter a number
    item_total = item_cost * item_count
    total = total + item_total
print("Total:",total)



