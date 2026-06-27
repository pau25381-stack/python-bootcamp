# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("Enter the price:"))
item_count_1 = int(input("Number of Items:"))
total1 = item_cost_1 * item_count_1

item_cost_2 = int(input("Enter the price:"))  # Let the user enter a number
item_count_2 = int(input("Number of Items:"))  # Let the user enter a number
total2 = item_cost_2 * item_count_2

item_cost_3 = int(input("Enter the price:"))  # Let the user enter a number
item_count_3 = int(input("Number of Items:"))  # Let the user enter a number
total3 = item_cost_3 * item_count_3

# Calculate the total
total = total1 + total2 + total3
print("Total:", total)