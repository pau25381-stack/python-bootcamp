def spend(expenses):
    """TODO: Add a new cost in expenses"""
    new_item_cost = int(input("Item cost: "))
    expenses.append(new_item_cost)

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    expenses.pop(-1)

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)
    print(sum(expenses))

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        if command == "refund":
            refund(current_expenses)
        if command == "show":
            show(current_expenses)
        if command == "exit":
            break


main()
