class CostTracker:
    def __init__(self):
        self.items = []
    def spend(self):
        expense = int(input("Enter expense: "))
        self.items.append(expense)
    def refund(self):
        self.items.pop(-1)
    def show(self):
        print(self.items)
        print("Total:", sum(self.items))
    def mainloop(self):
        running = True

        while running:
            command = input("Command: ")
            if command == "spend":
                self.spend()
            if command == "show":
                self.show()
            if command == "refund":
                self.refund()
            if command == "exit":
                break

cost_tracker = CostTracker()
cost_tracker.mainloop()
