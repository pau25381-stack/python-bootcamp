def add(inventory):
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """
    name = input("Enter item name: ")
    info = input("Enter item info: ")
    stock = input("Enter item stock: ")

    item = {
        "name": name,
        "info": info,
        "stock": stock
    }

    inventory.append(item)

def remove(inventory):
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """
    index = int(input("Enter item index: "))
    inventory.pop(index)

def read(inventory):
    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
    index = int(input("Enter item index: "))
    print(inventory[index])

def show(inventory):
    """TODO: Print items line-by-line"""
    for order in inventory:
        print("order:")
        for k, v in order.items():
            print(f"\t{k}: {v}")
    print()

def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            add(inventory)
            pass
        elif command == "remove":
            #  TODO: Use remove command"""
            remove(inventory)
            pass
        elif command == "read":
            # TODO: Use read command"""
            read(inventory)
            pass
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)
            pass
        elif command == "exit":
            running = False


main()
