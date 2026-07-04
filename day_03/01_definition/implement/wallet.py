class Wallet:
    def __init__(self, amount=0):
        self.amount = amount

wallet1 = Wallet(1000)
wallet2 = Wallet()

print(wallet1.amount)
print(wallet2.amount)