total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        number = int(input("Enter a number:")) # TODO: Ask for number
        total = total + number # TODO: Add that number to the total
        print (total) # TODO: Print the current total
        pass

    if command == "sub":
        number = int(input("Enter a number:")) # TODO: Ask for number
        total = total - number # TODO: subtract that number to the total
        print (total) # TODO: Print the current total
        pass

    elif command == "exit":
        running = False
